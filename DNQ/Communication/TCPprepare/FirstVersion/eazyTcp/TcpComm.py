# -*- coding:utf-8 -*-
#
# Python TCP服务器端练习
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
tcpServerSock = socket(AF_INET,SOCK_STREAM)
# 绑定至固定IP和端口
tcpServerSock.bind(ADDR)
tcpServerSock.listen(5)
# 监听并设置最大连接数限制

print('Waiting for connection......')


def tcplink(tcpCliSock, addr):
	print('Accept new connection from %s:%s...' % addr)
	tcpCliSock.send(b'Try Connection!')
	while True:
		data = tcpCliSock.recv(BUFSIZE)
		time.sleep(1)
		print(data.decode('utf-8'))
		if not data or data.decode('utf-8') == 'exit':
			break

		tcpCliSock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	tcpCliSock.close()
	print('Connection from %s:%s closed!' % addr)
	# tcpServerSock.close()

while True:
	tcpCliSock, addr = tcpServerSock.accept()
	newthread = threading.Thread(target=tcplink, args=(tcpCliSock, addr))
	newthread.start()



