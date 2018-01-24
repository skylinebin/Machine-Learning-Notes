# -*- coding:utf-8 -*-
#
# Python TCP客户端练习
#

from socket import *
import threading,time
from time import ctime

HOST = '127.0.0.1'
PORT = 21363
BUFSIZE = 1024
ADDR = (HOST,PORT)
# 初始化服务器地址和端口

# 创建基于IPV4和TCP协议的Socket
tcpClientSock = socket(AF_INET,SOCK_STREAM)
# 连接固定IP和端口
tcpClientSock.connect(ADDR)

for data in [b'bin', b'Tracy', b'Sarch']:
	tcpClientSock.send(data)

	print(tcpClientSock.recv(BUFSIZE).decode('utf-8'))

tcpClientSock.send(b'exit')
time.sleep(3)
tcpClientSock.close()
# 监听并设置最大连接数限制






