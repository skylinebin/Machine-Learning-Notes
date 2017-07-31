# coding=utf-8

import numpy as np

a = np.random.random((2,4))#随机生成２行４列的矩阵

b = np.random.random((3,3))#随机生成３行３列的矩阵

print(a)
print(np.sum(a))#求和
print(np.min(a))#求所有最小值
print(np.max(a))#求所有最大值

print(np.sum(a,axis=1))#axis=1表示每一行求和
print(np.sum(a,axis=0))#axis=0表示每一列求和
print(np.max(a,axis=1))#求每一行的最大值
print(np.min(a,axis=0))#求每一列的最小值


