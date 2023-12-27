echo "$USER   ALL=NOPASSWD: /usr/sbin/pm-suspend" >> /etc/sudoers.d/suspend
cp suspend.sh /usr/bin/suspend.sh
