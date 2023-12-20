import PySimpleGUI as sg
import os.path
import tkinter as tk
from utils import *
from ui.header import header
from ui.footer import footer
from ui.panels.home import Home
from ui.panels.files import Files
from ui.panels.settings import Settings

SCALING=2

font = ("Arial", 18)
sg.theme("Reddit")
sg.set_options(scaling=SCALING)

# Getting the screen size
root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

def create_window(panel):
    window = sg.Window('PyReaderOS', [header(), panel, footer()], no_titlebar=True, location=(0,0), size=(width,height), keep_on_top=True, font=font, element_justification="c").Finalize()
    window.TKroot["cursor"] = "none" 
    return window


PANEL = "HOME"

home = Home()
files = Files()
settings = Settings()

window = create_window(home.build())

while True:
    refresh = False
    event, values = window.read()

    print("Event", event)

    if event and event.startswith("ui-panel-files-"):
        refresh = refresh or files.handle(event, values)
    
    if event == "ui-panel-home-files":
        PANEL = "FILES"
        window.close()
        window = create_window(files.build())

    if event == "ui-panel-home-settings":
        PANEL = "SETTINGS"
        window.close()
        window = create_window(settings.build())

    elif event == "ui-footer-home":
        PANEL = "HOME"
        window.close()
        window = create_window(home.build())

    elif event == "ui-header-brightness":
        on_off_brightness()

    elif event == "ui-panel-settings-brightness-warm":
        set_brightness(int(values['ui-panel-settings-brightness-warm']), "warm")
        
    elif event == "ui-panel-settings-brightness-cold":
        set_brightness(int(values['ui-panel-settings-brightness-cold']), "cold")
        
    elif event == "QUIT" or event == sg.WIN_CLOSED:
        break

#    if refresh:
#        window.close()
#        create_window(files.build())

    window['ui-header-battery'].update(get_battery_percentage())

window.close()
