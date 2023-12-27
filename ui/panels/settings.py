import PySimpleGUI as sg
import nmcli
from ui.popup_manager import popup_manager
from utils import *

nmcli.disable_use_sudo()


class Settings():
    def __init__(self):
        self.name = "settings"
        self.general = nmcli.general()
        self.ssid = None
        return

    def update(self):
        wificonf = ""
        self.general = nmcli.general()
        for device in nmcli.device():
            net_conf = nmcli.device.show(device.device)
            if net_conf.get('GENERAL.TYPE') == 'wifi' and net_conf.get('GENERAL.STATE') == '100 (connected)':
                print(net_conf)
                self.ssid = net_conf.get('GENERAL.CONNECTION')
                wificonf += "MAC: " +net_conf['GENERAL.HWADDR'] + '\n'
                wificonf += "SSID: " + net_conf['GENERAL.CONNECTION'] + '\n'
                wificonf += "IPv4: " + (net_conf.get('IP4.ADDRESS[1]') if net_conf.get('IP4.ADDRESS[1]') else "") + '\n'
                wificonf += "IPv6: " + (net_conf.get('IP6.ADDRESS[1]') if net_conf.get('IP6.ADDRESS[1]') else "") + '\n'
        self.wificonf.update(wificonf)

        self.networks = []
        for net in nmcli.device.wifi():
            if net.ssid:
                self.networks.append(net)
        self.networks_list.update([ net.ssid for net in self.networks ])
            
        self.wifi_switch.update('ON' if self.general.wifi else "OFF", button_color=(("white", "black") if self.general.wifi else ("black", "white")))
        self.delete_conf.update(disabled=(not self.general.wifi))

        return

    def handle(self, event, values, window):
        if event == "ui-panel-settings-wifi-switch":
            wifi_on_off()

        elif event == "ui-panel-settings-brightness-warm":
            set_brightness(int(values['ui-panel-settings-brightness-warm']), "warm")

        elif event == "ui-panel-settings-brightness-cold":
            set_brightness(int(values['ui-panel-settings-brightness-cold']), "cold")

        elif event == "ui-panel-settings-wifi-delete":
            if self.ssid:
                nmcli.connection.delete(self.ssid)
                self.ssid = None

        elif event == "ui-panel-settings-wifi-networks":
            print('values', values)
            for network in self.networks:
                if network.ssid == values['ui-panel-settings-wifi-networks'][0]:
                    if network.ssid != self.ssid and "WPA" in network.security or "WEP" in network.security:
                        window.write_event_value("KEYBOARD", None)
                        passphrase = popup_manager.input('Type the Passphrase for %s.\n You won\'t see any output but each of your inputs is correctly saved.\n Press ENTER when you are finished.' %network.ssid)
                        print('PASSPHRASE', passphrase)
                        if passphrase:
                            try:
                                nmcli.device.wifi_connect(network.ssid, passphrase)
                            except Exception as e:
                                sg.popup("Connection activation failed. Make sure the passphrase is correct")
                                print(e)
                    elif network.ssid != self.ssid and len(network.security) == 0:
                        try:
                            nmcli.device.wifi_connect(network.ssid, '')
                        except Exception as e:
                            sg.popup("An error occured, could not connect to %s" %network.ssid)
                            print(e)
                        
            if self.ssid:
                print('connected to ', self.ssid)
        self.update()
        return

    def build(self):

        self.wificonf = sg.Text('')
        self.delete_conf = sg.Button('Forget Network', k="ui-panel-settings-wifi-delete", disabled=True)
        self.networks = []
        self.networks_list = sg.Listbox(self.networks, k="ui-panel-settings-wifi-networks", size=(100, 7), enable_events=True)
        self.wifi_switch = sg.Button('ON' if self.general.wifi else "OFF", key="ui-panel-settings-wifi-switch", button_color=(("white", "black") if self.general.wifi else ("black", "white"))) 
        self.layout =  [
            [ sg.Text('Brightness Warm') ],
            [ sg.Slider(range=(0, 255), default_value=get_brightness("warm"), expand_x=True, enable_events=True, orientation='horizontal', key='ui-panel-settings-brightness-warm', resolution=15, size=(50, 50)) ],
            [ sg.Text('Brightness Cold') ],
            [ sg.Slider(range=(0, 255), default_value=get_brightness("cold"), expand_x=True, enable_events=True, orientation='horizontal', key='ui-panel-settings-brightness-cold', resolution=15, size=(50, 50)) ],
            [ sg.Text('Wifi Status') ],
            [ self.wifi_switch ],
            [ sg.Text('Wifi Configuration') ],
            [ self.wificonf ],
            [ self.delete_conf ],
            [ sg.Text('Wifi Networks') ],
            [ self.networks_list ]
        ]
        
        self.column = sg.Column(self.layout, vertical_alignment='center', justification='center', k='settings-panel', expand_y=True, expand_x=True, visible=False, pad=(0, 0))
        return [ sg.pin(self.column) ]

    def show(self):
        self.column.update(visible=True)
        self.column.expand(True, True, True)

    def hide(self):
        self.column.update(visible=False)
        self.column.expand(False, False, False)
