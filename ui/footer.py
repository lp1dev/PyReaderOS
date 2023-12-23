import PySimpleGUI as sg
from pynput.keyboard import Key, Controller

class Footer():
    def __init__(self):
        self.name = "FOOTER"
        return

    def build(self):
        return [
            [
                sg.Button(image_filename='icons/left-arrow-solid-96.png', button_color="white", k="ui-footer-left", border_width=0),
                sg.Button(image_filename='icons/home-alt-2-solid-96.png', button_color="white", k="ui-footer-home", border_width=0),
                sg.Button(image_filename='icons/keyboard-solid-96.png', button_color="white", k="KEYBOARD", border_width=0),
                sg.Button(image_filename='icons/window-close-regular-96.png', button_color="white", k="CLOSE", border_width=0),
                sg.Button(image_filename='icons/exit-solid-96.png', button_color="white", k="QUIT", border_width=0),
                sg.Button(image_filename='icons/right-arrow-solid-96.png', button_color="white", k="ui-footer-right", border_width=0)
            ]
        ]

    def update(self):
        return

    def handle(self, event, values):
        if event == "ui-footer-left":
            kb = Controller()
            kb.press(Key.left)

        elif event == "ui-footer-right":
            kb = Controller()
            kb.press(Key.right)
        return
