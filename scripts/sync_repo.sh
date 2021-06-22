#!/usr/bin/bash
cd /root/eurosbot && git pull -q origin master
/root/eurosbot/venv/bin/pip install -r /root/eurosbot/requriments.txt
