# -*- coding:utf-8 -*-
#
# Python 客户端模拟接收数据练习
#

from socket import *
import threading,time
from time import ctime
import random

# HOST = '127.0.0.1'
HOST = '10.139.44.127'
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
	tempdata = str(tempa)+','+str(tempb)+','+'1'
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
connectstate =1
while True:
	if tcpClientSock.recv(BUFSIZE).decode('utf-8') == 'Start transfer':
		print("We will transfer our datas!")
		while True:
			getdata = randomdata()
			tcpClientSock.send(getdata.encode('utf-8'))
			processeddata = tcpClientSock.recv(BUFSIZE).decode('utf-8')
			time.sleep(1)
			if processeddata == 'End transfer':
				connectstate =0
				break
			CaculateArray.append(processeddata)
			print("Processed data:"+processeddata)

	if connectstate == 0:
		break


# for data in [b'bin', b'Tracy', b'Sarch']:
# 	tcpClientSock.send(data)
#
# 	print(tcpClientSock.recv(BUFSIZE).decode('utf-8'))

tcpClientSock.send(b'exit')
time.sleep(1)
tcpClientSock.close()
# 监听并设置最大连接数限制






