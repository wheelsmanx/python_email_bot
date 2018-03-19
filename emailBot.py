#By Justin Hagerty
#Date: 3/18/2018
# Python code to illustrate Sending mail 
# Notes include how to make this script a service in ubuntu

"""
what actually makes this repo is
the fact that I used upstart in ubuntu to make this
a service.

note if you are running ubuntu 16+
you must run first.

sudo apt-get install upstart-sysv

the reason being is that they did away with upstart in 16+ and replaced it
with systemd

1.) Make the file emailBot.conf in /etc/init

<beginFile>
description = "your description here"

start on runlevel [2345]
stop on runlevel [016]

respawn

//put this file here at this location
exec python /pythonScript/emailBot.py
</beginFile>

2.)run the command initctl reload-configuration

"""

import smtplib
import time 
 
# list of email_id to send the mail
li = ["justinshagerty@gmail.com"]

for i in range(len(li)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("", "")
    message = "Message_you_need_to_send"
    s.sendmail("wheelsmanx@gmail.com", li[i], message)
    s.quit

