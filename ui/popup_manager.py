import PySimpleGUI as sg
from pynput import keyboard
from time import sleep
import threading

class PopupManager():
    def __init__(self):
        self.listener = None
        self._buffer = ""
        return

    def on_keypress(self, key):
        try:
            self._buffer += key.char
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
            if key == keyboard.Key.enter:
                self.listener.stop()
            elif key == keyboard.Key.backspace:
                if len(self._buffer):
                   self. _buffer = self._buffer[:-1]

    def listen(self):
        with keyboard.Listener(on_press=self.on_keypress) as self.listener:
            self.listener.join()
        return

    def input(self, text):
        self._buffer = ""
        self.window = sg.Window(layout=[[ sg.Text(text) ]], title="popup", keep_on_top=True).Finalize()
        self.window.maximize()
        sleep(1)
        self.listen()
        self.window.close()
        return self._buffer

popup_manager = PopupManager()
