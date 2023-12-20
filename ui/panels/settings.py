import PySimpleGUI as sg
from utils import *

class Settings():
    def __init__(self):
        self.name = "SETTINGS"
        return

    def update(self):
        return

    def handle(self, event, values):
        return

    def build(self):
        return [
            sg.Column(
                [
                    [ sg.Text('Brightness Warm') ],
                    [ sg.Slider(range=(0, 255), default_value=get_brightness("warm"), expand_x=True, enable_events=True, orientation='horizontal', key='ui-panel-settings-brightness-warm', resolution=15) ],
                    [ sg.Text('Brightness Cold') ],
                    [sg.Slider(range=(0, 255), default_value=get_brightness("cold"), expand_x=True, enable_events=True, orientation='horizontal', key='ui-panel-settings-brightness-cold', resolution=15) ]
                ],
                vertical_alignment='center', justification='center', k='panel', expand_y=True, expand_x=True)
        ]
