echo "$USER   ALL=NOPASSWD: /usr/bin/suspend.sh" >> /etc/sudoers.d/suspend
cp suspend.sh /usr/bin/suspend.sh
dconf load /org/onboard/ < etc/onboard.conf
