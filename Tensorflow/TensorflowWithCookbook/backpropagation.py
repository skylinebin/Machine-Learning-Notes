# -*- coding:utf-8 -*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# only disables the AVX Warning

#
# 使用 Tensorflow 实现反向传播
# 主要使用回归算法来 调整变量
#
#

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

sess = tf.Session()
# 创建计算图会话

# 生成数据，创建占位符和变量 A
x_vals = np.random.normal(1, 0.1, 100)
y_vals = np.repeat(10., 100)
x_data = tf.placeholder(shape=[1], dtype=tf.float32)
y_target = tf.placeholder(shape=[1], dtype=tf.float32)
A =  tf.Variable(tf.random_normal(shape=[1]))

# 使用乘法
mul_output = tf.multiply(x_data, A)

# 计算 L2 正则损失函数
l2_loss = tf.square(mul_output - y_target)

# 初始化变量
init_var = tf.global_variables_initializer()
sess.run(init_var)

# 使用 梯度下降法作为优化器进行优化
gra_opt = tf.train.GradientDescentOptimizer(learning_rate=0.02)
train_step = gra_opt.minimize(l2_loss)
# 使用 梯度下降法按照 最小化 L2正则损失函数 进行训练

# 进行迭代训练

# 存储loss
loss_datas = []

for i in range(500):
    rand_index = np.random.choice(100)
    # 随机选取 x, y 传入计算图
    rand_x = [x_vals[rand_index]]
    rand_y = [y_vals[rand_index]]
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
    loss_datas.append(sess.run(l2_loss, feed_dict={x_data:rand_x, y_target: rand_y})[0])
    if (i+1)%100==0:
        print('Step #' + str(i+1) + ' A=' + str(sess.run(A))+ ' Loss = ' + str(sess.run(l2_loss, feed_dict={x_data:rand_x, y_target: rand_y})))


# 画出loss趋势图
plt.plot(np.arange(len(loss_datas)), loss_datas)
plt.ylabel('Loss')
plt.xlabel('training steps')
plt.show()