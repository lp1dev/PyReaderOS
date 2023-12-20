import PySimpleGUI as sg
from utils import *

def header():
    return [
        [
            sg.Text("PyReaderOS"),
            sg.Text("- Version 0.0.1 -"),
            sg.Button(image_filename='icons/brightness-half-regular-96.png', button_color="white", k="ui-header-brightness", image_subsample=2, border_width=0),
            sg.Button(image_filename='icons/battery-regular-96.png', button_color="white", border_width=0, image_subsample=2),
            sg.Text(get_battery_percentage(), k="ui-header-battery")]
    ]
