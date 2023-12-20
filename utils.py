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

