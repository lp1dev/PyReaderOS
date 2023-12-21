from tkhtmlview import html_parser
import PySimpleGUI as sg
from os import listdir, path
from tkhtmlview import html_parser

def set_html(widget, html, strip=True):
    prev_state = widget.cget('state')
    widget.config(state=sg.tk.NORMAL)
    widget.delete('1.0', sg.tk.END)
    widget.tag_delete(widget.tag_names)
    parser = html_parser.HTMLTextParser()
    parser.w_set_html(widget, html, strip=strip)
    widget.config(state=prev_state)

def get_battery_status():
    psus = listdir("/sys/class/power_supply/")
    for entry in psus:
        if ('-battery') in entry:
            values = listdir(path.join("/sys/class/power_supply/", entry))
            if "status" in values:
                with open(path.join("/sys/class/power_supply/", entry, "status")) as f:
                    status = f.read()
                    return status.replace("\n", "")    

def get_battery_percentage():
    psus = listdir("/sys/class/power_supply/")
    for entry in psus:
        if ('-battery') in entry or ('BAT') in entry:
            values = listdir(path.join("/sys/class/power_supply/", entry))
            if "capacity" in values:
                with open(path.join("/sys/class/power_supply/", entry, "capacity")) as f:
                    capacity = f.read()
                    return capacity.replace("\n", "")


def get_brightness(type="warm"):
    if path.isfile("/sys/class/backlight/backlight_%s/brightness" %type):
        with open("/sys/class/backlight/backlight_%s/brightness" %type) as f:
            return int(f.read().replace("\n", ""))
    else:
        print("ELSE", type)
        dirs = listdir("/sys/class/backlight/")
        for d in dirs:
            with open("/sys/class/backlight/%s/brightness" %d) as f:
                return int(f.read().replace("\n", ""))
            
def set_brightness(value, type="warm"):
    if path.isfile("/sys/class/backlight/backlight_%s/brightness" %type):
        with open("/sys/class/backlight/backlight_%s/brightness" %type, "w+") as f:
            f.write(str(value))
            return value
    else:
        dirs = listdir("/sys/class/backlight/")
        for d in dirs:
            with open("/sys/class/backlight/%s/brightness" %d, "w+") as f:
                f.write(str(value))
                return value
                
def on_off_brightness():
        current_value = get_brightness("warm")
        if current_value > 0:
            set_brightness(0, "warm")
            set_brightness(0, "cold")
        else:
            set_brightness(100, "warm")
            set_brightness(100, "cold")
