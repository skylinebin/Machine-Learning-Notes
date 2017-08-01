'''# _*_ coding:UTF-8  _*_ '''
# coding:utf-8

#学习使用numpy分割矩阵

import numpy as np

A = np.arange(12).reshape((3,4))

print(A)


print(np.split(A,2,axis=1))#纵向分割
print(np.split(A,3,axis=0))#横向分割

print(np.split(A,4,axis=1))#纵向分割，不能直接不等分割


print(np.array_split(A,3,axis=1))#纵向不等分割

print(np.vsplit(A,3))#纵向分割

print(np.hsplit(A,2))#横向分割
