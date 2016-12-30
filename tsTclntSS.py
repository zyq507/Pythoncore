# -*- coding: utf-8 -*-
from socket import *

HOST = 'localhost'
PORT = 21569
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('>')
    if not data:
        break
    tcpCliSock.send(('%s \r\n' % data).encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data.strip())
    tcpCliSock.close()
