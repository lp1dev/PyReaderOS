import PySimpleGUI as sg
from utils import *

def settings():
    return [
        sg.Column(
            [
                [sg.Text('Brightness Warm'), sg.Slider(range=(0, 255), default_value=get_brightness("warm"), expand_x=True, enable_events=True, orientation='horizontal', key='ui-panel-settings-brightness-warm', resolution=15) ],
                [sg.Text('Brightness Cold'), sg.Slider(range=(0, 255), default_value=get_brightness("cold"), expand_x=True, enable_events=True, orientation='horizontal', key='ui-panel-settings-brightness-cold', resolution=15) ]
            ],
            vertical_alignment='center', justification='center', k='panel')
    ]
