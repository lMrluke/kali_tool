import subprocess
from multiprocessing import Pool
import threading
from scapy.all import *


a = subprocess.check_output("ifconfig | grep eth0 -A1 | grep inet | awk '{print $2}'| cut -d '.' -f 1,2,3 ",shell=True)

def test(ip):
    answer = sr1(IP(dst=ip)/ICMP(),timeout=0.1,verbose=0)
    if answer == None:
        #print(ip + " is not exist")
        pass
    else:
        print(ip + " is exist")



po = Pool(20)

b = a.decode("utf-8")
c = b.strip()
for i in range(0,20):
    ip = c +"."+str(i)
    po.apply_async(test,(ip,))


print("=======start=========")
po.close()
po.join()
print("=========end=========")
