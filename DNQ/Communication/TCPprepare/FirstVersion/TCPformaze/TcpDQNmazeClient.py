# -*- coding:utf-8 -*-
#
# DQN TCP 客户端模拟接收数据并改变环境
#

import gym
from socket import *
import threading,time
from maze_env import Maze
# env = gym.make('MountainCar-v0')
# env = env.unwrapped
env = Maze()
import numpy as np

# print(env.action_space)
# print(env.observation_space)
# print(env.observation_space.high)
# print(env.observation_space.low)

HOST = '10.139.44.127'
PORT = 21363
BUFSIZE = 1024
ADDR = (HOST,PORT)
# 初始化服务器地址和端口

# 创建基于IPV4和TCP协议的Socket
tcpClientSock = socket(AF_INET,SOCK_STREAM)
# 连接固定IP和端口
tcpClientSock.connect(ADDR)

tcpClientSock.send(('Data transfer request').encode('utf-8'))

def processobservation(observation):
	changedobser = ""
	for evnum in observation:
		# print(evnum)
		changedobser+= str(round(evnum,8))+":"
	changedobser+='1'
	return changedobser

def run_maze():
	total_step = 0
	for i_episode in range(300):
		observation = env.reset()
		ep_r = 0
		reward =0.0
		tempdone = False
		observation_ = np.array([0.0,0.0])
		Epsilon = 0.0
		tcpClientSock.send(('endoneturn').encode('utf-8'))
		checkstate = 1
		while True:
			if checkstate == 1:
				env.render()
				checkstate =0
			processeddata = tcpClientSock.recv(BUFSIZE).decode('utf-8')#获取从缓存中读取的TCP数据
			if (processeddata == 'ok'):
				changedobser = processobservation(observation)
				tcpClientSock.send(changedobser.encode('utf-8'))
			if(processeddata[-1] == '1'):
				thisaction = int(processeddata[0])
				observation_,reward,done = env.step(thisaction)
				# position,velocity = observation_
				# reward = abs(position - (-0.5))
				tempdone = done
				backstring = str(observation)+':'+str(thisaction)+':'+str(reward)+':'+str(observation_)+':2'
				print("backstring:",backstring)
				tcpClientSock.send(backstring.encode('utf-8'))

			if(processeddata == 'storeok'):
				thisstep = str(total_step)+':3'
				tcpClientSock.send(thisstep.encode('utf-8'))

			if(processeddata[-1] == '3'):
				tempdatalist = str(processeddata).split(':')
				Epsilon = float(tempdatalist[0])
				tcpClientSock.send(('endoneturn').encode('utf-8'))
				checkstate = 1

			# print(processeddata[-1],processeddata[0])
			if checkstate == 1:
				# ep_r += reward
				observation = observation_
				if tempdone:
					print('Epi:',i_episode,'| Ep_r:',round(ep_r,4),'| Epsilon:',round(Epsilon,2))
					break
				total_step+= 1
	env.destroy()



connectstate =1
while True:
	getdatas = tcpClientSock.recv(BUFSIZE).decode('utf-8')
	# print("getdatas:",getdatas)
	if getdatas == 'Start transfer':
		print("We will transfer our datas!")


		env.after(100, run_maze)
		env.mainloop()

	if connectstate == 0:
		break

# for i_episode in range(10):
# 	observation = env.reset()
#






tcpClientSock.send(b'exit')
time.sleep(1)
tcpClientSock.close()