# -*- coding:utf-8 -*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# only disables the AVX Warning

#
# 使用 Tensorflow 实现反向传播
# 主要使用分类算法
# sigmoid 函数将正态分布分割成不同的两类
# 试图找到一个优化转换方式A，它可以把两个正态分布转换到原点
#

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.python.framework import ops
ops.reset_default_graph()

sess = tf.Session()
# 创建计算图会话

# 生成数据，创建占位符和变量 A
# 从正态分布 N(-1, 1) 和 N(3, 1) 生成数据
x_vals = np.concatenate((np.random.normal(-1, 1, 50), np.random.normal(3, 1, 50)))
# print(x_vals) # 均值为 -1 的正态分布 和 均值为 3 的正态分布
y_vals = np.concatenate((np.repeat(0., 50), np.repeat(1., 50)))
# print(y_vals) # 随机生成 50个 0 和 50 个 1
x_data = tf.placeholder(shape=[1], dtype=tf.float32)
y_target = tf.placeholder(shape=[1], dtype=tf.float32)
A =  tf.Variable(tf.random_normal(mean=10,shape=[1]))
# 初始化变量 A 为 10 附近的值，远离理论值-1


# 转换操作
add_output = tf.add(x_data, A)

# 增加维度
add_output_expanded = tf.expand_dims(add_output, 0)
y_target_expanded = tf.expand_dims(y_target, 0)


# 初始化变量
init_var = tf.global_variables_initializer()
sess.run(init_var)

# 要在初始化变量之后，输出初始化的A值
print('initial A: ' + str(sess.run(A)))
print('-----------------------')

# 声明Sigmoid交叉熵损失函数
xentropy_loss = tf.nn.sigmoid_cross_entropy_with_logits(logits=add_output_expanded, labels=y_target_expanded)
# 传入的参数需要指定的维度，所以需要提前增加维度


# 使用 梯度下降法作为优化器进行优化
gra_opt = tf.train.GradientDescentOptimizer(learning_rate=0.05)
train_step = gra_opt.minimize(xentropy_loss)
# 使用 梯度下降法按照 最小化 Sigmoid交叉熵损失函数 进行训练
# 让 Tensorflow 知道如何更新和偏差变量


# 进行迭代训练，更新变量 A
# 声明变量存储 loss
loss_data = []
for i in range(1800):
    rand_index = np.random.choice(100)
    # 随机选取 x, y 传入计算图
    rand_x = [x_vals[rand_index]]
    rand_y = [y_vals[rand_index]]
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
    # 存储 loss 值
    loss_data.append(sess.run(xentropy_loss, feed_dict={x_data:rand_x, y_target: rand_y})[0][0])

    # 每隔200次输出一次
    if (i+1)%200==0:
        print('Step #' + str(i+1) + ' A=' + str(sess.run(A))+ ' Loss = ' + str(sess.run(xentropy_loss, feed_dict={x_data:rand_x, y_target: rand_y})))


# 画出loss趋势图
plt.plot(np.arange(len(loss_data)), loss_data)
plt.ylabel('Cost')
plt.xlabel('training steps')
plt.show()