import PySimpleGUI as sg
import os.path
import tkinter as tk

from utils import *
from ui.header import Header
from ui.footer import Footer
from ui.panels.home import Home
from ui.panels.files import Files
from ui.panels.library import Library
from ui.panels.settings import Settings
from process_handler import process_handler
from conf import SCALING, TOP_BAR_SIZE, BOTTOM_BAR_SIZE, KEYBOARD_SIZE

CURRENT_PANEL = None

font = ("Arial", 14)
sg.theme("Reddit")
sg.set_options(scaling=SCALING)
sg.set_options(sbar_width=50)
sg.set_options(sbar_arrow_width=50)

# Getting the screen size
root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.withdraw()

header = Header()
footer = Footer()
home = Home(desktop_loader())
files = Files()
library = Library(height - BOTTOM_BAR_SIZE - TOP_BAR_SIZE, width)
settings = Settings()
processes = []

def init_windows():
    top_bar = sg.Window("BottomBar", [ header.build() ], no_titlebar=True, location=(0, 0), keep_on_top=True, size=(width, TOP_BAR_SIZE), element_justification="c", font=font).Finalize()
    bottom_bar = sg.Window("Bar", [ footer.build() ], no_titlebar=True, location=(0, height - BOTTOM_BAR_SIZE), keep_on_top=True, size=(width, BOTTOM_BAR_SIZE), element_justification="c", font=font).Finalize()
    window = sg.Window('PyReaderOS', [ settings.build(), files.build(), library.build(), home.build() ], no_titlebar=True, location=(0, TOP_BAR_SIZE), size=(width,height - bottom_bar.size[1] - top_bar.size[1]), keep_on_top=False, font=font, element_justification="c").Finalize()
    home.show()
    window.TKroot["cursor"] = "none"
    bottom_bar.TKroot["cursor"] = "none"
    top_bar.TKroot["cursor"] = "none"
    return top_bar, bottom_bar, window

def switch_panel(panel):
    global CURRENT_PANEL
    if panel != CURRENT_PANEL:
        CURRENT_PANEL.hide()
        CURRENT_PANEL = panel
        CURRENT_PANEL.show()

top_bar, bottom_bar, window = init_windows()

CURRENT_PANEL = home
KEYBOARD_UP = False
KEYBOARD_PID = 0

header.update()

while True:
    refresh = False
    window, event, values = sg.read_all_windows()
    print("Event", event)

    if event and event.startswith("ui-panel-files-"):
        files.handle(event, values)

    elif event and event.startswith("ui-panel-home-"):
        home.handle(event, values)

    elif event and event.startswith("ui-panel-library-"):
        library.handle(event, values)
        
    elif event and event.startswith("ui-header-"):
        header.handle(event, values)

    elif event and event.startswith("ui-footer-"):
        footer.handle(event, values)

        
    if event == "ui-panel-home-files":
        switch_panel(files)
        
    elif event == "ui-panel-home-settings":
        switch_panel(settings)

    elif event == "ui-panel-home-library":
        switch_panel(library)

    elif event == "ui-footer-home":
        switch_panel(home)

    elif event == "ui-panel-settings-brightness-warm":
        set_brightness(int(values['ui-panel-settings-brightness-warm']), "warm")
        
    elif event == "ui-panel-settings-brightness-cold":
        set_brightness(int(values['ui-panel-settings-brightness-cold']), "cold")

    elif event == "KEYBOARD":
        if KEYBOARD_UP:
            KEYBOARD_UP = False
            process_handler.kill(KEYBOARD_PID)
        else:
            KEYBOARD_UP = True
            KEYBOARD_PID = start_process("onboard", f"onboard -s {width}x{KEYBOARD_SIZE} -x 0 -y {height - BOTTOM_BAR_SIZE - KEYBOARD_SIZE}")


    elif event == "CLOSE":
        process_handler.close()

    elif event == "QUIT" or event == sg.WIN_CLOSED:
        break

    header.update()

window.close()
