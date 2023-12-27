import PySimpleGUI as sg

from os import listdir, path, environ
from process_handler import process_handler

ebooks = [ "pdf", "epub", "mobi", "txt", "rtf" ]

class Library():
    def __init__(self, height, width):
        self.name = "library"
        self.path = path.join(environ['HOME'], "Documents")
        self.height = height
        self.width = width
        return

    def build(self):

        files = []
        for f in listdir(self.path):
            filepath = path.join(self.path, f)
            if path.isfile(filepath):
                files.append(f)
                print('found document', f)

        self.text = sg.Text('Available documents')
        self.list = sg.Listbox(files, expand_x=True, expand_y=True, enable_events=True, key='ui-panel-library-list', size=(100, 12), font=('Arial Bold', 24))

        self.column = sg.Column([
                [ self.text ],
                [ self.list ]
            ],
                                vertical_alignment='center', justification='center', k='panel-library', visible=False)
        return [ sg.pin(self.column) ] 

        
    def handle(self, event, values, window):

        if event == "ui-panel-library-list":
            selected = values['ui-panel-library-list'][0]
            if selected.split(".")[1] in ebooks:
                process_handler.start("mupdf", f"mupdf -S 34 -W {self.width} -H {self.height} {path.join(self.path, selected)}")

    def hide(self):
        self.column.update(visible=False)

    def show(self):
        self.column.update(visible=True)
                
    def update(self):
        return
