#Author : Rsecurity

import socket

s = socket.socket()

ip = (input("Please enter the Ip: "))
port = str(input("Enter the Port: "))

s.connect((ip, int(port)))

print(s.recv(1024))
s.close()