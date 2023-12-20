import PySimpleGUI as sg

def home():
    return [
        sg.Column(
            [[
                sg.Button('Settings', k="ui-panel-home-settings"),
                sg.Button('Browser'),
                sg.Button('Files', k="ui-panel-home-files"),
                sg.Button('Gallery'),
                sg.Button('Misc')
            ]],
            vertical_alignment='center', justification='center', k='panel')
    ]