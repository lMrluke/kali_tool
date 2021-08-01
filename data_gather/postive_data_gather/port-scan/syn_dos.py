import subprocess
#from multiprocessing import Pool
#import threading
from concurrent.futures import ThreadPoolExecutor
from scapy.all import *

f = open("/root/kali_tool/data_gather/postive_data_gather/second_layer/scrapy/result.txt","w") 


a = subprocess.check_output("ifconfig | grep eth0 -A1 | grep inet | awk '{print $2}'| cut -d '.' -f 1,2 ",shell=True)

co = 0
def test(ip):
    global co
    answer = sr1(IP(dst=ip)/TCP(flags="S"),timeout=1,verbose=0)
    if answer == None:
        #print(ip + " is not exist")
        pass
    else:
        print(ip + " is send")




b = a.decode("utf-8")
c = b.strip()

def test2(i):
    pool = ThreadPoolExecutor(max_workers=100)
    while(1):
        for q in range(1,255):
            for w in range(1,255):
                ip = c +"."+str(q)+"."+str(w)
                pool.submit(test,(ip))
            

if __name__ == "__main__":
    test2(1)


