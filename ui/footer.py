import PySimpleGUI as sg
from pynput.keyboard import Key, Controller, KeyCode
from process_handler import process_handler

class Footer():
    def __init__(self):
        self.name = "FOOTER"
        return

    def build(self):
        return [
            [
                sg.Button(image_filename='icons/left-arrow-solid-96.png', button_color="white", k="ui-footer-left", border_width=0),
                sg.Button(image_filename='icons/zoom-out-solid-96.png', button_color="white", k="ui-footer-zoomout", border_width=0),
                sg.Button(image_filename='icons/home-alt-2-solid-96.png', button_color="white", k="ui-footer-home", border_width=0),
                sg.Button(image_filename='icons/keyboard-solid-96.png', button_color="white", k="KEYBOARD", border_width=0),
                sg.Button(image_filename='icons/window-close-regular-96.png', button_color="white", k="CLOSE", border_width=0),
                sg.Button(image_filename='icons/exit-solid-96.png', button_color="white", k="ui-footer-refocus", border_width=0),
                sg.Button(image_filename='icons/zoom-in-solid-96.png', button_color="white", k="ui-footer-zoomin", border_width=0),
                sg.Button(image_filename='icons/right-arrow-solid-96.png', button_color="white", k="ui-footer-right", border_width=0)
            ]
        ]

    def update(self):
        return

    def handle(self, event, values):
        active_process = process_handler.last()
        kb = Controller()
        if event == "ui-footer-left":
            if active_process.get('name') == "mupdf":
                kb.press(KeyCode.from_char("b"))
                kb.release(KeyCode.from_char("b"))
            elif active_process.get('name') == "dillo":
                kb.press(KeyCode.from_char(","))
                kb.release(KeyCode.from_char(","))
        elif event == "ui-footer-right":
            if active_process.get('name') == "mupdf":
                kb.press(Key.space)
                kb.release(Key.space)
            elif active_process.get('name') == "dillo":
                kb.press(KeyCode.from_char("."))
                kb.release(KeyCode.from_char("."))
        elif event == "ui-footer-zoomin":
            kb.press(KeyCode.from_char("+"))
            kb.release(KeyCode.from_char("+"))
        elif event == "ui-footer-zoomout":
            kb.press(KeyCode.from_char("-"))
            kb.release(KeyCode.from_char("-"))
        elif event == "ui-footer-refocus":
            kb.press(Key.cmd)
            kb.press(KeyCode.from_char("c"))

            kb.release(Key.cmd)
            kb.release(KeyCode.from_char("c"))

        return
