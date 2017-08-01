'''# _*_ coding : UTF-8 _*_'''
#coding=utf-8

#学习一些numpy中基本的矩阵运算函数

import numpy as np
import pandas as pd

A = np.arange(14,2,-1).reshape((3,4)) #定义步长是－１　
#从14降序到２并初始化形状位３行４列的矩阵
print(A)

print(np.argmin(A)) #打印最小值的索引,第０位
print(np.argmax(A)) #打印最大值的索引,第11位

print(np.mean(A)) #打印矩阵的平均值 7.5
print(A.mean()) #或者这么用 矩阵的平均值7.5
print(np.average(A)) #另一种求平均值

print(np.median(A)) #求矩阵的中位数

print(np.cumsum(A)) #逐步累加

print(np.diff(A)) #两个数的垒差

print(np.nonzero(A))#输出非零的行数和列数

print(np.sort(A))#输出每一行的行排序

print(np.transpose(A))#输出矩阵的反向
print(A.T)#输出矩阵的反向
print((A.T).dot(A))#输出矩阵的反向与原矩阵矩阵相乘

print(np.clip(A,5,9)) #将小于５的数变成５将大于９的数变成９

# 所有的矩阵运算都能指定是对于行计算或者是对于列计算
print(np.mean(A,axis=0))# 求矩阵Ａ每一列的平均值
print(np.mean(A,axis=1))# 求矩阵Ａ每一行的平均值

