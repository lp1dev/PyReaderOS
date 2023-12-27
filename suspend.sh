#!/bin/sh

DISPLAY=:0
FILE="$HOME/.asleep"

if [ -f "$FILE" ];then
    killall feh
    echo "1" > /sys/class/leds/e60k02:white:on/brightness
    brightnessctl -d "backlight_warm" s $(sed -n 0p $FILE)
    brightnessctl -d "backlight_cold" s $(sed -n 1p $FILE)
    sleep 2
    echo 1-0024 | tee /sys/bus/i2c/drivers/cyttsp5/unbind
    sleep 2
    echo 1-0024 | tee /sys/bus/i2c/drivers/cyttsp5/bind
    rm $FILE
else
    dbus-send --type=method_call --print-reply --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide
    feh -Y -x -q -D5 -B white -F -Z -z -r /home/lp1/Pictures/&
    touch $FILE
    brightnessctl -d "backlight_warm" g >> $FILE
    brightnessctl -d "backlight_cold" g >> $FILE
    brightnessctl -d "backlight_warm" s 0
    brightnessctl -d "backlight_cold" s 0
    echo "0" > /sys/class/leds/e60k02:white:on/brightness
    sleep 5
    pm-suspend
fi
