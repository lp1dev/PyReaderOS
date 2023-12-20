import PySimpleGUI as sg

from os import listdir, path

class Files():
    def __init__(self):
        self.path = "/"
        self.sg = None
        return

    def build(self):

        self.buffer = []
        self.paths = listdir(self.path)
        self.paths.append("..")
    
        self.list = sg.Listbox(self.paths, expand_x=True, expand_y=True, enable_events=True, key='ui-panel-files-list')
        self.text_path = sg.Text('Current path : '+self.path)
        self.text_file = sg.Text('Opened file : ')
        self.file_contents = sg.Listbox(self.buffer, expand_x=True, expand_y=True, horizontal_scroll=True)

        return [
            sg.Column([
                [ self.text_path ],
                [ self.list ],
                [ self.text_file ],
                [ self.file_contents ],
            ],
                      vertical_alignment='center', justification='center', k='panel', expand_x=True)
        ]

    def openfile(self, filepath):
        with open(filepath) as f:
            self.buffer = [ line.replace("\n", "") for line in f.readlines() ]
            self.file_contents.update(self.buffer)
        
    def handle(self, event, values):
        if event == "ui-panel-files-list":
            filepath = path.join(self.path, self.list.get()[0])
            if path.isdir(filepath):
                self.path = filepath
                self.paths = listdir(self.path)
                self.paths.append("..")
                self.text_path.update('Current path : '+ filepath)
                self.list.update(self.paths)
            else:
                self.text_file.update('Opened file : '+ filepath)
                self.openfile(filepath)

    def update(self):
        return
