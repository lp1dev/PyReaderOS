import PySimpleGUI as sg
from process_handler import process_handler
#from utils import *

class Home():
    def __init__(self, desktop_entries):
        self.desktop_entries = desktop_entries
        self.name = "home"
        return

    def pin(self, item):
        return sg.pin(item)
    
    def build(self):
        IMAGE_SIZE = 200
        static_layout = [
            [
                sg.Button("\n\n\nBooks", button_color=("black", "white"), image_filename='icons/book-solid-96.png', k="ui-panel-home-library", image_size=(IMAGE_SIZE, IMAGE_SIZE), border_width=0),
                sg.Button("\n\n\nSettings", image_filename='icons/cog-solid-120.png', k="ui-panel-home-settings", image_size=(IMAGE_SIZE, IMAGE_SIZE), button_color=("black", "white"), border_width=0),
                sg.Button("\n\n\nFiles", image_filename='icons/folder-open-solid-120.png', k="ui-panel-home-files", image_size=(IMAGE_SIZE, IMAGE_SIZE), button_color=("black", "white"), border_width=0),
                sg.Button("\n\n\nGallery", image_filename='icons/image-alt-solid-120.png', k="ui-panel-home-gallery", image_size=(IMAGE_SIZE, IMAGE_SIZE), button_color=("black", "white"), border_width=0)
            ]
        ]

        dynamic_layout = [[]]
        for index, entry in enumerate(self.desktop_entries):
            button = sg.Button("\n\n\n%s" %entry['Name'], image_filename=entry['Icon'], k="ui-panel-home-%s" %index, image_size=(IMAGE_SIZE, IMAGE_SIZE), button_color=("black", "white"), border_width=0)
            dynamic_layout[0].append(button)

        self.layout = []
        for row in static_layout + dynamic_layout: # Seems to actually do something for buttons positionning
            l_row = []
            for item in row:
                l_row.append(self.pin(item))
            self.layout.append(l_row)

        self.column = sg.Column(self.layout, vertical_alignment='top', justification='center', k='home-panel', expand_x=True, expand_y=True)
        self._pin = sg.pin(self.column)
        return [ self._pin ]

    def hide(self):
        self.column.update(visible=False)

    def show(self):
        self._pin.expand(True, True, True)
        self.column.update(visible=True)
    
    def update(self):
        return
    
    def handle(self, event, values, window):
        index = event.replace("ui-panel-home-", "")
        if index.isnumeric():
            entry = self.desktop_entries[int(index)]
            process_handler.start(entry['Name'], entry['Exec'])
        return
    

