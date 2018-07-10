# -*- coding:utf-8 -*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# only disables the AVX Warning

#
# 使用 Tensorflow 实现各种损失函数
#
#

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


sess = tf.Session()
# 创建一个会话

# first: 回归算法的损失函数

# 创建预测序列和目标序列作为张量
x_vals = tf.linspace(-1., 1., 500)
target = tf.constant(0.)


# 1. L2正则损失函数(欧拉损失函数)
l2_y_vals = tf.square(target - x_vals)
l2_y_out = sess.run(l2_y_vals)

# same as (t1-x1)^2 + .... +(tn-xn)^2
# Tensorflow内建L2正则形式，nn.l2_loss() = 1/2 * l2_y_vals


# 2. L1正则损失函数(绝对值损失函数)
l1_y_vals = tf.abs(target - x_vals)
l1_y_out = sess.run(l1_y_vals)
# same as |t1-x1| + .... +|tn-xn|


# 3.Pseudo-Huber 损失函数
delta1 = tf.constant(0.25)
phuber1_y_vals = tf.multiply(tf.square(delta1), tf.sqrt(1. + tf.square((target - x_vals)/delta1)) - 1.)
phuber1_y_out = sess.run(phuber1_y_vals)

delta2 = tf.constant(5.)
phuber2_y_vals = tf.multiply(tf.square(delta2), tf.sqrt(1. + tf.square((target - x_vals)/delta2)) - 1.)
phuber2_y_out = sess.run(phuber2_y_vals)


x_vals = tf.linspace(-3., 5., 500)
target = tf.constant(1.)
# targets = tf.fill([500,], 1.)


# 4.Hinge损失函数
hinge_y_vals = tf.maximum(0., 1. - tf.multiply(target, x_vals))
hinge_y_out = sess.run(hinge_y_vals)
# 主要用来评估支持向量机算法
# 上述算法使目标值为1，预测值距离1越近，损失函数值越小



# 5.Cross-entropy loss 两类交叉熵损失函数(逻辑损失函数)
xentropy_y_vals = - tf.multiply(target, tf.log(x_vals)) - tf.multiply((1. - target), tf.log(1. - x_vals))
xentropy_y_out = sess.run(xentropy_y_vals)
# same as -(t * log(x)) - [(1 - t) * log(1 - x)]


# x_vals = tf.linspace(-3., 5., 500)
# target = tf.constant(1.)
targets = tf.fill([500,], 1.)

# 6.Sigmoid交叉熵损失函数
xentropy_sigmoid_vals = tf.nn.sigmoid_cross_entropy_with_logits(logits=x_vals, labels=targets)
xentropy_sigmoid_out = sess.run(xentropy_sigmoid_vals)
# 先将x_vals值通过sigmoid函数转换,再计算交叉熵损失


# 7.加权交叉熵损失函数(Weighted cross entropy loss)
weight = tf.constant(0.5)
xentropy_weighted_y_vals = tf.nn.weighted_cross_entropy_with_logits(targets, x_vals, weight)
xentropy_weighted_y_out = sess.run(xentropy_weighted_y_vals)
# 是Sigmoid交叉熵损失函数 的加权，对正目标加权


# 8.Softmax交叉熵损失函数(Softmax cross entropy loss)
unscaled_logits = tf.constant([[1., -3., 10.]])
target_dist = tf.constant([[0.1, 0.02, 0.88]])
softmax_xentropy = tf.nn.softmax_cross_entropy_with_logits_v2(labels=unscaled_logits, logits=target_dist)
print(sess.run(softmax_xentropy))

# 只针对单个目标分类计算损失,通过 softmax 函数将输出结果转化成概率分布


# 9.稀疏Softmax 交叉熵损失函数
unscaled_logits = tf.constant([[1., -3., 10.]])
sparse_target_dist = tf.constant([2])
sparse_xentropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=unscaled_logits, labels=sparse_target_dist)
print(sess.run(sparse_xentropy))
# 把目标分类为true 转化成 index



print('----------------------')

# 使用 matplotlib 绘制回归算法的损失函数

# part1

# x_array = sess.run(x_vals)
# plt.plot(x_array, l2_y_out, 'b-', label='L2 Loss')
# plt.plot(x_array, l1_y_out, 'r--', label='L1 Loss')
# plt.plot(x_array, phuber1_y_out, 'k-.', label='P-Huber Loss (0.25)')
# plt.plot(x_array, phuber2_y_out, 'g:', label='P-Huber Loss (5.0)')
# plt.ylim(-0.2, 0.4)
# plt.legend(loc='lower right', prop={'size': 11})
# plt.show()



# part2
x_array = sess.run(x_vals)
plt.plot(x_array, hinge_y_out, 'b-', label='Hinge Loss')
plt.plot(x_array, xentropy_y_out, 'r--', label='Cross-entropy loss')
plt.plot(x_array, xentropy_sigmoid_out, 'k-.', label='Cross-entropy sigmoid loss')
plt.plot(x_array, xentropy_weighted_y_out, 'g:', label='Weighted Cross-entropy loss')
plt.ylim(-1.5, 3)
plt.legend(loc='lower right', prop={'size': 11})
plt.show()





