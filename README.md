# python_email_bot
python bot that I am working on to test a linux service - while the service runs it should send an email every couple of min or so 

## how to run and "install" this 
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
