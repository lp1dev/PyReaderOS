from os import listdir, path

def get_battery_percentage():
    psus = listdir("/sys/class/power_supply/")
    for entry in psus:
        if ('-battery') in entry:
            values = listdir(path.join("/sys/class/power_supply/", entry))
            if "capacity" in values:
                with open(path.join("/sys/class/power_supply/", entry, "capacity")) as f:
                    capacity = f.read()
                    return capacity.replace("\n", "")


def get_brightness(type="warm"):
    with open("/sys/class/backlight/backlight_%s/brightness" %type) as f:
        return int(f.read().replace("\n", ""))
            
def set_brightness(value, type="warm"):
    with open("/sys/class/backlight/backlight_%s/brightness" %type, "w+") as f:
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
