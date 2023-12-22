import PySimpleGUI as sg
import os.path
import tkinter as tk

from utils import *
from ui.header import Header
from ui.footer import footer
from ui.panels.home import Home
from ui.panels.files import Files
from ui.panels.settings import Settings

SCALING=2
TAB_SIZE = 100
CURRENT_PANEL = None

font = ("Arial", 18)
sg.theme("Reddit")
sg.set_options(scaling=SCALING)

# Getting the screen size
root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.withdraw()

header = Header()
home = Home()
files = Files()
settings = Settings()

def init_windows():
    tab = sg.Window("Bar", [ footer() ], no_titlebar=True, location=(0, height - TAB_SIZE), keep_on_top=True, size=(width, TAB_SIZE), element_justification="c").Finalize()
    window = sg.Window('PyReaderOS', [header.build(), settings.build(), files.build(), home.build() ], no_titlebar=True, location=(0,0), size=(width,height - tab.size[1]), keep_on_top=False, font=font, element_justification="c").Finalize()
    home.show()
    window.TKroot["cursor"] = "none"
    return tab, window

def switch_panel(panel):
    global CURRENT_PANEL
    if panel != CURRENT_PANEL:
        CURRENT_PANEL.hide()
        CURRENT_PANEL = panel
        CURRENT_PANEL.show()


tab, window = init_windows()

CURRENT_PANEL = home

header.update()

while True:
    refresh = False
    window, event, values = sg.read_all_windows()
    print("Event", event)

    if event and event.startswith("ui-panel-files-"):
        files.handle(event, values)
        
    elif event and event.startswith("ui-header-"):
        header.handle(event, values)
    
    if event == "ui-panel-home-files":
        switch_panel(files)
        
    if event == "ui-panel-home-settings":
        switch_panel(settings)

    elif event == "ui-footer-home":
        switch_panel(home)

    elif event == "ui-panel-settings-brightness-warm":
        set_brightness(int(values['ui-panel-settings-brightness-warm']), "warm")
        
    elif event == "ui-panel-settings-brightness-cold":
        set_brightness(int(values['ui-panel-settings-brightness-cold']), "cold")
        
    elif event == "QUIT" or event == sg.WIN_CLOSED:
        break

    header.update()

window.close()
