#!/bin/bash

python3 /root/kali_tool/data_gather/postive_data_gather/second_layer/scrapy/re_arp.py

nmap -v -p 139,445 -iL /root/kali_tool/data_gather/postive_data_gather/second_layer/scrapy/result.txt | tee result
