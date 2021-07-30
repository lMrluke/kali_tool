#!/bin/bash

# --scan is scan the port of destinate 
# -S is use the syn flags

hping3 ${1} --scan 1-200 -S



hping3 -c 200 -S --spoof 172.18.3.33 -p ++1 ${1}

