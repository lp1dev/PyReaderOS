import PySimpleGUI as sg
import os.path
import tkinter as tk
from utils import *
from ui.header import header
from ui.footer import footer
from ui.panels.home import home
from ui.panels.files import files

font = ("Arial", 30)

sg.theme("Reddit")

def create_window(panel):
    window = sg.Window('PyReaderOS', [header(), panel(), footer()], no_titlebar=True, location=(0,0), size=(width,height), keep_on_top=True, font=font, element_justification="c").Finalize()
    window['panel'].expand(True, True, True)
    return window

# Getting the screen size
root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

PANEL = "HOME"

window = create_window(home)

while True:
    event, values = window.read()

    print(event)
    if event == "ui-panel-home-files":
        PANEL = "FILES"
        window.close()
        window = create_window(files)
    elif event == "ui-footer-home":
        PANEL = "HOME"
        window.close()
        window = create_window(home)
        
    elif event == "QUIT" or event == sg.WIN_CLOSED:
        break
    window['ui-header-battery'].update("Battery: %s" %get_battery_percentage())

window.close()
