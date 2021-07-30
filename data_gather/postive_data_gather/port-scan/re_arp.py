import subprocess
#from multiprocessing import Pool
#import threading
from concurrent.futures import ThreadPoolExecutor
from scapy.all import *

f = open("/root/kali_tool/data_gather/postive_data_gather/second_layer/scrapy/result.txt","w") 


a = subprocess.check_output("ifconfig | grep eth0 -A1 | grep inet | awk '{print $2}'| cut -d '.' -f 1,2,3 ",shell=True)

co = 0
def test(ip):
    global co
    answer = sr1(ARP(pdst=ip),timeout=0.1,verbose=0)
    if answer == None:
        #print(ip + " is not exist")
        pass
    else:
        print(ip + " is exist")
        f.write(ip + "\n")




b = a.decode("utf-8")
c = b.strip()

def test2(i):
    pool = ThreadPoolExecutor(max_workers=20)
    while(i < 50):
        ip = c +"."+str(i)
        pool.submit(test,(ip))
        i = i + 1

if __name__ == "__main__":
    test2(1)


