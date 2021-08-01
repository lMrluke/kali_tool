
import socket


banner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
banner.connect(("172.18.3.1",23))
data  = banner.recv(1024)
print(data.encoding=="utf-8")
print("ok")
