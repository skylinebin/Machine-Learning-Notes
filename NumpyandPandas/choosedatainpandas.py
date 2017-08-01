'''# _*_ coding : UTF-8 _*_'''
# coding=utf-8

#学习Pandas选择数据

import numpy as np
import pandas as pd

#会输出dtype数据类型
dates = pd.date_range('20130101',periods=6)
print(dates)

df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['a','b','c','d'])
#生成有名称的数据
print(df)

print(df['a'])#输出第a列

print(df.a)#另一种不同选出第a列

print(df[0:3],df['20130102':'20130104'])

#select by label:loc
print(df.loc['20130102'])
print(df.loc['20130102',['a','b']])#打印指定列的参数

#select by position:iloc
print(df.iloc[3])#打印第三行数据

print(df.iloc[1:3,1:3])#筛选行列均为2，3的数据

print(df.iloc[[1,3,5],1:3])

#mixed selection : ix
print(df.ix[:3,['a','c']])#混合筛选

#Boolean indexing
print(df[df.a > 8])#筛选所有a中大于8的数据，其他也显示