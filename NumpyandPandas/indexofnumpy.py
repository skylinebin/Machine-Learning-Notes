'''# _*_ coding : UTF-8 _*_'''
# coding=utf-8

#学习　numpy　的索引　20170801

import numpy as np

B = np.arange(3,15)
A = np.arange(3,15).reshape((3,4))

print(B)

print(B[3]) #打印索引的第＇３＇个值,实际是第四个:0,1,2,3

print(A)

#所有的索引都是从　０　１　２　３　开始的,无论是行还是列
# [[ 3  4  5  6]
#  [ 7  8  9 10]
#  [11 12 13 14]]
# 上面第1行第1列　是　８
# 第2行第1列　是　12

print(A[2]) #索引出第三行:0,1,2

print(A[1][1])# 第1行第1列 8
print(A[2][1])# 第2行第1列 
print(A[2,1])# 也可以写成第2行第1列 

print(A[2,:])#打印第2行的所有矩阵数据(第0,1,2行)
print(A[:,1])#打印第1列的所有矩阵数据(第0,1,2列)
print(A[1,1:3])#打印第1行从１:3的数据(第0,1,2行)

for row in A:
	print(row)#打印出每一行

print(A.T)
for column in A.T:
	print(column) #打印每一列，因为没有直接对列操作的函数，
	#就先将矩阵转置，再对行操作就是对原来的列操作

print(A.flatten()) #将矩阵展开的函数,转换成一行一列的矩阵
#A.flat是一个迭代器,是一个对象属性，返回会是一个内存地址
for item in A.flat:
	print(item) #迭代出矩阵中的每一项

