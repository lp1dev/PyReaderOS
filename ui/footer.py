import PySimpleGUI as sg

def footer():
    return [
        [sg.Button('HOME', k="ui-footer-home"), sg.Button('Action 2'), sg.Button('QUIT')]
    ]
