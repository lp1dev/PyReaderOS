import PySimpleGUI as sg

def files():
    return [
        sg.Column(
            [[
                sg.Text('Files')
            ]],
            vertical_alignment='center', justification='center', k='panel')
    ]
