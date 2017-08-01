''' _*_ coding:UTF-8 _*_ '''
# coding:utf-8

#numpy的赋值情况学习

import numpy as np

a = np.arange(4)

b = a #a与b关联起来 无论a,b哪一个改变，另外一个也跟着变

c = a

d = b

a[0] = 11

print(a)

print(b is a)


print(b)
print(c)
print(d)

#在python中赋值，后面的都等于a

d[1:3] = [22,33]
#a,b,c,d都会改变

#如果只是赋值，不将b和a关联,则使用copy
b = a.copy() #deep copy 复制但不关联