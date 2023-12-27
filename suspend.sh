#!/bin/sh

FILE="$HOME/.asleep"

if [ -f "$FILE" ];then
    notify-send "Waking up"
    rm $FILE
    echo "1" > /sys/class/leds/e60k02:white:on/brightness
    brightnessctl -d "backlight_warm" s $(sed -n 0p $FILE)
    brightnessctl -d "backlight_cold" s $(sed -n 1p $FILE)
    echo 1-0024 | sudo tee /sys/bus/i2c/drivers/cyttsp5/unbind
    sleep 1
    echo 1-0024 | sudo tee /sys/bus/i2c/drivers/cyttsp5/bind
else
    notify-send "Suspending..."
    touch $FILE
    echo "0" > /sys/class/leds/e60k02:white:on/brightness
    brightnessctl -d "backlight_warm" g > $FILE
    brightnessctl -d "backlight_cold" g > $FILE
    brightnessctl -d "backlight_warm" s 0
    brightnessctl -d "backlight_cold" s 0
    
    sleep 1
    sudo pm-suspend
fi
