# -*- coding:utf-8 -*-
#
# Python TCP客户端练习
#

from socket import *
import threading,time
from time import ctime
import random

HOST = '127.0.0.1'
PORT = 21363
BUFSIZE = 1024
ADDR = (HOST,PORT)
# 初始化服务器地址和端口

def randomdata():
	mina = 2
	maxa = 10
	minb = 5
	maxb = 20
	tempa = random.randint(mina,maxa)
	tempb = random.randint(minb,maxb)
	tempdata = '('+tempa+','+tempb+','+'1)'
	if tempb == 20:
		tempdata = 'exit'
	print(tempdata)
	return tempdata


CaculateArray = []

# 创建基于IPV4和TCP协议的Socket
tcpClientSock = socket(AF_INET,SOCK_STREAM)
# 连接固定IP和端口
tcpClientSock.connect(ADDR)

tcpClientSock.send(('Data transfer request').encode('utf-8'))

if tcpClientSock.recv(BUFSIZE).decode('utf-8') == 'Start transfer':
	while True:
		getdata = randomdata()
		tcpClientSock.send(getdata.encode('utf-8'))
		processeddata = tcpClientSock.recv(BUFSIZE).decode('utf-8')
		time.sleep(1)
		if processeddata == 'End transfer':
			break
		CaculateArray.append(processeddata)
		print("Processed data:"+processeddata)


# for data in [b'bin', b'Tracy', b'Sarch']:
# 	tcpClientSock.send(data)
#
# 	print(tcpClientSock.recv(BUFSIZE).decode('utf-8'))

tcpClientSock.send(b'exit')
time.sleep(3)
tcpClientSock.close()
# 监听并设置最大连接数限制






