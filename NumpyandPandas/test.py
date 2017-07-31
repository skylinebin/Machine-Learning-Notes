#! python3
# coding=utf-8

import numpy as np
import pandas as pd

a = np.array([[1,1],[0,1]])
b = np.arange(4).reshape((2,2))#reshape对矩阵形状进行重构
print(a)
print(b)
c = a*b #逐个相乘
d = np.dot(a,b) #矩阵相乘

d_dot_two = a.dot(b)
print(c)
print(d)
print(d_dot_two)
# a = np.array([10,20,30,40])
# b = np.arange(4)

# print(a,b)
# c = b**2
# d = 10*np.sin(a)
# print('xiangjian:',c)
# print(d)

# print(b)
# print(b<3)

