# CaS - Command and Script

Tested on: Debian/Ubuntu based dists.

## How to use

    1. Navigate on terminal to where you download cas.py  (cd /folder)
    2. Enter on terminal: sudo python3 cas.py
    3. Follow the instructions on terminal

## Features
    - Run regular linux terminal commands on background.
    - Create scripts with terminal commands to run using cron
        - Scripts created use a .lock file to prevent run commands alredy running 

### Why use it?:
    - Command rclone to copy your cloud drive to a local folder without occupying terminal
    - Make a script with terminal commands to easily add to cron
    

## Bugs
    You need to recreate the script if you need to move it to another folder. (due to path of .lock file)