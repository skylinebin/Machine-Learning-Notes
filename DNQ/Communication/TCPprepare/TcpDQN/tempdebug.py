# -*- coding:utf-8 -*-
#
# 	处理数据测试
#

import numpy as np


def getoriarray(olddata):
	print("first:",olddata)
	olddata = olddata[1:-1]
	print("after:",olddata)
	datalist = olddata.split(' ')
	checknumpy = np.array([1.0,2.0])
	checknumpy[0] = float(datalist[0])
	checknumpy[1] = float(datalist[1]+'0')
	return checknumpy





# teststr = "[-5.91565906e-01 -4.97425391e-04]:1:0.0915571023168108:[-5.91557102e-01  8.80318615e-06]:2"
teststr = "[-0.50766171  0.        ]:0:0.008781194345100496:[-0.50878119 -0.00111948]:2"
storedataList = teststr.split(':')
print(storedataList)
print(storedataList[0])
testarray = np.array([1.0,2.0])
observation = np.array(storedataList[0])
print('observation:',observation)
thisaction = int(storedataList[1])
print('this action:',thisaction)
thisreward = float(storedataList[2])
print('thisreward:',thisreward)
observation_ = np.array(storedataList[3])
print("observation_:",observation_)
print("--------------------")
observation = getoriarray(storedataList[0])
print("afterObservation:",observation)

changedobser = ""
for evnum in observation:
	print(evnum)
	changedobser+= str(round(evnum,8))+":"
changedobser+='1'
print(changedobser)


