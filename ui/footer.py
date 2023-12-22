import PySimpleGUI as sg

def footer():
    return [
        [
            sg.Button(image_filename='icons/home-alt-2-solid-96.png', button_color="white", k="ui-footer-home", border_width=0),
            sg.Button(image_filename='icons/keyboard-solid-96.png', button_color="white", k="KEYBOARD", border_width=0),
            sg.Button(image_filename='icons/window-close-regular-96.png', button_color="white", k="CLOSE", border_width=0),
            sg.Button(image_filename='icons/exit-solid-96.png', button_color="white", k="QUIT", border_width=0)
        ]
    ]
