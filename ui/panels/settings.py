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

        self.layout =  [
            [ sg.Text('Brightness Warm') ],
            [ sg.Slider(range=(0, 255), default_value=get_brightness("warm"), expand_x=True, enable_events=True, orientation='horizontal', key='ui-panel-settings-brightness-warm', resolution=15, size=(50, 50)) ],
            [ sg.Text('Brightness Cold') ],
            [ sg.Slider(range=(0, 255), default_value=get_brightness("cold"), expand_x=True, enable_events=True, orientation='horizontal', key='ui-panel-settings-brightness-cold', resolution=15, size=(50, 50)) ]
        ]
        
        self.column = sg.Column(self.layout, vertical_alignment='center', justification='center', k='settings-panel', expand_y=True, expand_x=True, visible=False, pad=(0, 0))
        return [ sg.pin(self.column) ]

    def show(self):
        self.column.update(visible=True)
        self.column.expand(True, True, True)

    def hide(self):
        self.column.update(visible=False)
        self.column.expand(False, False, False)
