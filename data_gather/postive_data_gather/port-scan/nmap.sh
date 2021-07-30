#!/bin/bash

rm result 2>/dev/null
python3 /root/kali_tool/data_gather/postive_data_gather/second_layer/scrapy/re_arp.py

nmap -iL /root/kali_tool/data_gather/postive_data_gather/second_layer/scrapy/result.txt -p 1-100 >> result


