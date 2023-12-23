import PySimpleGUI as sg
from utils import *
from conf import VERSION
import nmcli

nmcli.disable_use_sudo()

class Header():
    def __init__(self):
        self.name = "HEADER"
        return

    def update(self):
        general = nmcli.general()
        battery_percentage = get_battery_percentage()
        battery_status = get_battery_status()
        
        self.battery_percentage.update("%s %%" %battery_percentage)
    
        if battery_status == "Charging":
            self.battery_button.update(image_filename="icons/battery-charging-solid-96.png", image_subsample=2)
        elif int(battery_percentage) > 50:
            self.battery_button.update(image_filename="icons/battery-solid-96.png", image_subsample=2)
        elif int(battery_percentage) > 20:
            self.battery_button.update(image_filename="icons/battery-low-solid-96.png", image_subsample=2)
        else:
            self.battery_button.update(image_filename="icons/battery-regular-96.png", image_subsample=2)

        if general.wifi:
            self.wifi_button.update(image_filename='icons/wifi-regular-96.png', image_subsample=2)
        else:
            self.wifi_button.update(image_filename='icons/wifi-off-regular-96.png', image_subsample=2)

        if get_brightness(type="warm") + get_brightness(type="cold") == 0:
            self.brightness_button.update(image_filename='icons/brightness-half-regular-96.png', image_subsample=2)
        else:
            self.brightness_button.update(image_filename='icons/brightness-half-solid-96.png', image_subsample=2)
        return
    
    def handle(self, event, values):
        if event == "ui-header-brightness":
            on_off_brightness()
        if event == "ui-header-wifi":
            wifi_on_off()
        return
    
    def build(self):
        self.brightness_button = sg.Button(image_filename='icons/brightness-half-regular-96.png', button_color="white", k="ui-header-brightness", image_subsample=2, border_width=0)
        self.battery_button = sg.Button(image_filename='icons/battery-regular-96.png', button_color="white", border_width=0, image_subsample=2)
        self.wifi_button = sg.Button(image_filename='icons/wifi-off-regular-96.png', button_color="white", border_width=0, image_subsample=2, k="ui-header-wifi")
        self.battery_percentage = sg.Text("%s %%" %get_battery_percentage(), k="ui-header-battery")
        return [
            [
                sg.Text("PyReaderOS"),
                sg.Text(f"- Version {VERSION} -"),
                self.wifi_button,
                self.brightness_button,
                self.battery_button,
                self.battery_percentage
            ]
        ]
