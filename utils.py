import PySimpleGUI as sg
from os import listdir, path, environ
import subprocess
import nmcli

nmcli.disable_use_sudo()

def kobo_led_brightness(value="1"):
    if path.isfile("/sys/class/leds/e60k02:white:on/brightness"):
        with open("/sys/class/leds/e60k02:white:on/brightness", "w+") as f:
            f.write("%s\n" %value)

def desktop_loader(desktop_path="%s/Desktop" %environ['HOME']):
    items = []
    for f in listdir(desktop_path):
        if path.isfile(path.join(desktop_path, f)) and f.endswith(".desktop"):
            with open(path.join(desktop_path, f)) as _f:
                entry = {}
                lines = _f.readlines()
                for line in lines:
                    if "=" in line:
                        line = line.replace("\n", "").split('=')
                        entry[line[0]] = line[1]
                items.append(entry)
    print(items)
    return items

def wifi_on_off():
    general = nmcli.general()
    start_process("nmcli", "nmcli radio wifi %s" %("off" if general.wifi else "on"))

def start_process(name, path):
    if " " in path:
        path = path.split(' ')
    process = subprocess.Popen(path, shell=False)
    return process.pid

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
