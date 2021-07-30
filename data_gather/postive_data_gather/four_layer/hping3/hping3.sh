#!/bin/bash

rm result.txt 2>/dev/null
rm r.txt 2>/dev/null
				
ip_add=172.18.3
for addr in $(seq 1 10);do
				hping3 $ip_add.$addr --udp -c 1 >> r.txt 2>/dev/null
done
echo "accomplish!"
grep "Unreachable" r.txt | cut -d ' ' -f 5 | cut -d '=' -f 2 >> result.txt
rm r.txt
