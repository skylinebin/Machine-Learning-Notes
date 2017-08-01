'''# _*_ coding : UTF-8 _*_'''
# coding=utf-8

# 学习pandas基础使用功能

import numpy as np
import pandas as pd

s = pd.Series([1,2,6,np.nan,45,9])
print(s)
#会输出dtype数据类型
dates = pd.date_range('20160101',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
#生成有名称的数据
print(df)
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)#未给出索引，默认添加数字

df2 = pd.DataFrame({
	'A':1.,
	'B':pd.Timestamp('20130102'),
	'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo'
	})
print(df2)#输出定义好的数据字典
print(df2.dtypes)#输出每一列的数据类型
print(df2.index)#输出每一行的索引名字
print(df2.columns)#输出每一列的名字
print(df2.values)#输出每一行的值

print(df2.describe())#运算数字形式的运算组

print(df2.T)#翻倒,行变成列，列变成行

print(df2.sort_index(axis=1,ascending=False))#列索引进行排序

print(df2.sort_values(by='E'))#根据值进行排序'E'

