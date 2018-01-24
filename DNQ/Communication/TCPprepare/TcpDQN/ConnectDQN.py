# -*- coding:utf-8 -*-
#
# TCP服务器端融合DQN练习
#

from socket import *
import threading,time

HOST = '10.139.44.127'
PORT = 21363
BUFSIZE = 1024
DataArray = []




def tcplink(tcpCliSock, addr):
	print('Accept new connection from %s:%s...' % addr)
	tcpCliSock.send(b'Try Connection!')
	DataIndex = 0
	while True:
		data = tcpCliSock.recv(BUFSIZE)
		time.sleep(1)
		print(data.decode('utf-8'))
		if data.decode('utf-8') == 'Data transfer request':
			tcpCliSock.send(('Start transfer').encode('utf-8'))
			DataIndex =1

		if DataIndex == 1 and data.decode('utf-8') != 'exit':
			DataArray.append(data.decode('utf-8'))
			print('Received:'+data.decode('utf-8'))
			tcpCliSock.send(('101').encode('utf-8'))



		if not data or data.decode('utf-8') == 'exit':
			DataIndex = 0
			break

		# tcpCliSock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	tcpCliSock.close()
	print('Connection from %s:%s closed!' % addr)


def initcp():
# HOST = '127.0.0.1'
	ADDR = (HOST,PORT)
	# 创建基于IPV4和TCP协议的Socket
	tcpServerSock = socket(AF_INET,SOCK_STREAM)
	# 绑定至固定IP和端口
	tcpServerSock.bind(ADDR)
	tcpServerSock.listen(5)
	# 监听并设置最大连接数限制

	tcpCliSock, addr = tcpServerSock.accept()
	newthread = threading.Thread(target=tcplink, args=(tcpCliSock, addr))
	newthread.start()





if __name__ == '__main__':
    initcp()
