# -*- coding:utf-8 -*-
#
# DQN TCP服务器端模拟处理数据练习
#

from RL_brain import DeepQNetwork

from socket import *
import threading,time
import numpy as np

RL = DeepQNetwork(n_actions=3,n_features=2,learning_rate=0.001,e_greedy=0.9,replace_target_iter=300,memory_size=3000,e_greedy_increment=0.0001)

total_step = 0


HOST = '10.139.44.127'
PORT = 21363
BUFSIZE = 1024
DataArray = []

def getoriarray(olddata):
	olddata = olddata[1:-1]
	datalist = olddata.split(' ')
	checknumpy = np.array([1.0,2.0])
	checknumpy[0] = float(datalist[0])
	checknumpy[1] = float(datalist[1]+'0')
	return checknumpy

def Rlstore(datas):
	storedataList = datas.split(':')
	# observation = np.array([1.0,2.0])
	# observation_ = np.array([1.0,2.0])
	observation = getoriarray(storedataList[0])
	thisaction = int(storedataList[1])
	thisreward = round(float(storedataList[2]),14)
	observation_ = getoriarray(storedataList[3])
	# print(storedataList)
	# print("observation_:",observation, thisaction, thisreward, observation_)
	RL.store_transition(observation,thisaction,thisreward,observation_)
	storeback = 'storeok'

	return storeback

def getaction(datas):
	observation = np.array([1.0,2.0])
	dataList = datas.split(':')
	# print(dataList)
	observation[0] = float(dataList[0])
	observation[1] = float(dataList[1])
	# observation[0] = dataList[0]
	# observation[1] = dataList[1]
	# print("observation:",observation)
	action = RL.choose_action(observation)
	# print("This is action:",action)
	return action


def tcplink(tcpCliSock, addr):
	print('Accept new connection from %s:%s...' % addr)
	tcpCliSock.send(b'Try Connection!')
	DataIndex = 0
	tcpCliSock.send(('ok').encode('utf-8'))
	while True:
		data = tcpCliSock.recv(BUFSIZE)
		time.sleep(1)
		print(data.decode('utf-8'))
		datas = bytes.decode(data)
		if DataIndex == 1 and datas != 'exit':
			# DataArray.append(data.decode('utf-8'))
			# print('Received:'+data.decode('utf-8'))
			# backdata = processdata(data)

			if(data.decode('utf-8')[-1]=='1'):
				backdata = str(getaction(datas)) + " 1"
				tcpCliSock.send(str(backdata).encode('utf-8'))

			if(data.decode('utf-8')[-1]=='2'):
				getdatas = str(Rlstore(datas))
				tcpCliSock.send(str(getdatas).encode('utf-8'))

			if(data.decode('utf-8')[-1]=='3'):
				templist = datas.split(':')
				tempi = int(templist[0])
				if tempi > 1000:
					RL.learn()
				rebackdata = str(RL.epsilon) + ":3"
				# print('rebackdata:',rebackdata)
				tcpCliSock.send(str(rebackdata).encode('utf-8'))


		if datas == 'Data transfer request':
			tcpCliSock.send(('Start transfer').encode('utf-8'))
			DataIndex =1

		if not datas or datas == 'exit':
			tcpCliSock.send(('End transfer').encode('utf-8'))
			DataIndex = 0
			break
		if datas == 'endoneturn':
			tcpCliSock.send(('ok').encode('utf-8'))

		# tcpCliSock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	time.sleep(3)
	tcpCliSock.close()
	print('Connection from %s:%s closed!' % addr)

	for everyd in DataArray:
		print(everyd)


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
	print("Waiting for connection....")
	newthread.start()





if __name__ == '__main__':
    initcp()



