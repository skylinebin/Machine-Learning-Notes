# -*- coding:utf-8 -*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# only disables the AVX Warning

#
# 用于实现两层计算图，第一层为Moving_Avg_Window，第二层为 Custom_Layer
# 并对各层layer和操作进行层级命名管理
#

import tensorflow as tf
import numpy as np


sess = tf.Session()
# 创建一个会话

# start 多层layer计算图

x_shape = [1, 4, 4, 1]
x_val = np.random.uniform(size=x_shape)

# 计算图中创建占位符，占位符用于传入图片
x_data = tf.placeholder(tf.float32, shape=x_shape)

# 创建滑动窗口和过滤器以及步长，使用conv2d()函数进行处理
my_filter = tf.constant(0.25, shape=[2, 3, 1, 1])
my_strides = [1, 2, 2, 1]
mov_avg_layer = tf.nn.conv2d(x_data, my_filter, my_strides, padding='SAME''', name='Moving_Avg_Windows')

# Output = (W - F + 2P)/S + 1
# W是输入形状，F是过滤器形状，P是padding的大小，S是步长形状

def custom_layer(input_matrix):
    input_matrix_sqeezed = tf.squeeze(input_matrix)
    A = tf.constant([[1., 2.], [-1., 3.]])
    b = tf.constant(1., shape=[2, 2])
    temp1 = tf.matmul(A, input_matrix_sqeezed)
    temp = tf.add(temp1, b)
#     A*x + b x为输入图片(矩阵)
    return (tf.sigmoid(temp))

with tf.name_scope('Custom_Layer') as scope:
    custom_layer1 = custom_layer(mov_avg_layer)

print(sess.run(custom_layer1, feed_dict={x_data: x_val}))
writer = tf.summary.FileWriter('logs/',sess.graph)

# end 多层layer计算图