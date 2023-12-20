import PySimpleGUI as sg
from utils import *

def header():
    return [
        [
            sg.Text("PyReaderOS"),
            sg.Text("- Version 0.0.1 -"),
            sg.Button("Brightness", k="ui-header-brightness"),
            sg.Text(get_battery_percentage(), k="ui-header-battery")
        ]
    ]
