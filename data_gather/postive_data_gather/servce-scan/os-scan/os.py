from  scapy.all import *
import sys

def main(ip):
    a = sr1(IP(dst=ip)/ICMP(),timeout=1,verbose=0)
    if a[IP].ttl <= 64 :
        print(str(ip) + " is linux")
    elif(a[IP].ttl > 64):
        print(str(ip) + " is windows")
    else:
        print("error")


if __name__ == "__main__":
    main(sys.argv[1])
