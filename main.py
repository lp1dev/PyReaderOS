import PySimpleGUI as sg
import os.path

font = ("Arial", 30)

sg.theme("Reddit")

header = [
    [sg.Text("PyReaderOS", font=font), sg.Text("- Version 0.0.1")]
]

contents = [
    sg.Column(
        [[sg.Button('Settings'), sg.Button('Browser'), sg.Button('Files'), sg.Button('Gallery'), sg.Button('Misc')]],
        vertical_alignment='center', justification='center', k='-C-')
]

footer = [
    [sg.Button('Action 1'), sg.Button('Action 2'), sg.Button('QUIT')]
]

layout = [
    header,
    contents,
    footer
]

# Create the window
import tkinter as tk

root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

window = sg.Window('PyReaderOS', layout, no_titlebar=True, location=(0,0), size=(width,height), keep_on_top=True, font=font, element_justification="c").Finalize()
window['-C-'].expand(True, True, True)


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "QUIT" or event == sg.WIN_CLOSED:
        break

window.close()
