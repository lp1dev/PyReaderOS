import PySimpleGUI as sg

from os import listdir, path

class Files():
    def __init__(self):
        self.path = "/"
        self.sg = None
        return

    def build(self):

        self.paths = listdir(self.path)
        self.paths.append("..")
    
        self.list = sg.Listbox(self.paths, expand_x=True, expand_y=True, enable_events=True, key='ui-panel-files-list')
        self.text = sg.Text('Current path : '+self.path)
        return [
            sg.Column([
                [ self.text ],
                [ self.list ]
            ],
            vertical_alignment='center', justification='center', k='panel')
        ]

    def handle(self, event, values):
        if event == "ui-panel-files-list":
            self.path = path.join(self.path, self.list.get()[0])
            self.paths = listdir(self.path)
            self.paths.append("..")
            self.text.update('Current path : '+self.path)
            self.list.update(self.paths)

    def update(self):
        return
