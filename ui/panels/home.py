import PySimpleGUI as sg

class Home():
    def __init__(self):
        self.name = "HOME"
        return

    def build(self):
        return [
            sg.Column(
                [
                    [
                        sg.Button(image_filename='icons/book-solid-96.png', button_color="white", k="ui-panel-home-library", image_size=(150, 150), expand_x=True, expand_y=True),
                    ],
                    [
                        sg.Button(image_filename='icons/cog-solid-120.png', button_color="white", k="ui-panel-home-settings", image_size=(150, 150), expand_x=True, expand_y=True),
                        sg.Button(image_filename='icons/world-regular-120.png', button_color="white", k="ui-panel-home-browser", image_size=(150, 150), expand_x=True, expand_y=True),
                    ],
                    [
                        sg.Button(image_filename='icons/folder-open-solid-120.png', button_color="white", k="ui-panel-home-files", image_size=(150, 150), expand_x=True, expand_y=True),
                        sg.Button(image_filename='icons/image-alt-solid-120.png', button_color="white", k="ui-panel-home-gallery", image_size=(150, 150), expand_x=True, expand_y=True),
                    ]
                ],
                vertical_alignment='center', justification='center', k='panel', expand_x=True, expand_y=True)
        ]
        
    
    def update(self):
        return
    
    def handle(self, event, values):
        return
    

