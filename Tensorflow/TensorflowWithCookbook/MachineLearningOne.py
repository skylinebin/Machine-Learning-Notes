# -*- coding:utf-8 -*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# only disables the AVX Warning

import tensorflow as tf
import numpy as np


sess = tf.Session()
# 创建一个会话


# start:针对简单乘法部分

# x_vals = np.array([1.,3.,5.,7.,9.])
# x_data = tf.placeholder(tf.float32)
# m_const = tf.constant(3.)
# my_product = tf.multiply(x_data, m_const)
# for x_val in x_vals:
#     print(sess.run(my_product, feed_dict={x_data: x_val}))

# end:针对简单乘法部分



# start 同一计算图进行多次乘法操作
# 嵌入层计算图

my_array = np.array([[1.,3.,5.,7.,9.],[-2.,0.,2.,4.,6.],[-6.,-3.,0.,3.,6.]])
xy_vals = np.array([my_array, my_array + 1])
xy_data = tf.placeholder(tf.float32, shape=(3,5))
m1 = tf.constant([[1.],[0.],[-1.],[2.],[4.]])
m2 = tf.constant([[2.]])
a1 = tf.constant([[10.]])

# 表示计算图
prod1 = tf.matmul(xy_data, m1)
prod2 = tf.matmul(prod1, m2)

add1 = tf.add(prod2, a1)

for x_val in xy_vals:
    print(sess.run(add1, feed_dict={xy_data: x_val}))


# end 同一计算图进行多次乘法操作




# 占位符仅声明变量的位置，用于传入数据到计算图
writer = tf.summary.FileWriter('logs/',sess.graph)