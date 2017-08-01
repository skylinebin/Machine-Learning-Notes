''' _*_ coding:UTF-8 _*_'''
# coding:utf-8

#学习将不同矩阵合并起来

import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])

C = np.vstack((A,B)) #vertical stack 上下合并

print(A.shape, C.shape)
#C.shape打印出了C矩阵的大小
print(C)#合并之后的C矩阵
D = np.hstack((A,B)) #horizontal stack　左右合并

print(A.shape, D.shape)
print(D)#合并之后的D矩阵
print(A.T) #一行矩阵转置后还是本来的那一行矩阵

print(A[np.newaxis,:].shape)#在前面加了一个维度
print(A[np.newaxis,:])#在前面加了一个维度


print(A[:,np.newaxis].shape)#在后面加了一个维度
print(A[:,np.newaxis])#在后面加了一个维度 变成纵向的111

E = A[:,np.newaxis]
F = B[:,np.newaxis]
I = np.hstack((E,F)) #horizontal stack　左右合并
print(E)
print(F)
print(I)


Cs = np.concatenate((E,F,E,F),axis=0)#纵向合并
print(Cs)
Cd = np.concatenate((E,F,E,F),axis=1)#横向合并
print(Cd)