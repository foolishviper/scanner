#!/usr/bin/python3 

import socket
import sys
import os

target = input("Enter the hostname or Ip:\n")
#Resolving a hostname to ip
try:
	ip_addr = socket.gethostbyname(target)
	print("You have entered {} hostname and the ip of the target is {}\n".format(target,ip_addr))
except socket.gaierror as e:
	print({e})
	sys.exit()


start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the end port: "))

#identify if the ip is up or down 
 
print("Please wait...Checking if the host is up or down!!\n")

response = os.system("ping -c 4 "+ ip_addr)
if response ==0:
	print("\nYour host {} is up".format(ip_addr))
else:
	print("\nYour host {} is down".format(ip_addr))
	sys.exit()

#port scanning:

for port in range(start_port, end_port+1):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	con = s.connect_ex((ip_addr,port))
	if(not con):
		print("Port {}: open".format(port))
	s.close()