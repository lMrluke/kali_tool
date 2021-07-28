import subprocess
from scapy.all import *


a = subprocess.check_output("ifconfig | grep eth0 -A1 | grep inet | awk '{print $2}'| cut -d '.' -f 1,2,3 ",shell=True)


b = a.decode("utf-8")
c = b.strip()
for i in range(0,255):
    ip = c +"."+str(i)
    answer = sr1(ARP(pdst=ip),timeout=0.1,verbose=0)
    if answer == None:
        print(ip + " is not exist")
    else:
        print(ip + " is exist")
