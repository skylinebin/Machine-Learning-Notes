# -*- coding:utf-8 -*-

import tensorflow as tf
import numpy as np

# 1.创建矩阵及其相关操作

indentity_matrix = tf.diag([1.0, 1.0, 1.0])
matrix_A = tf.truncated_normal([2, 3])
matrix_B = tf.fill([2,3], 5.0)
matrix_C = tf.random_uniform([3,2])
matrix_D = tf.convert_to_tensor(np.array([[1., 2., 3.],[-3., -7., -1.],[0., 5., -2.]]))

sess = tf.Session()

print(sess.run(indentity_matrix))
print('- - - - - - - - - - - - - - - - - - - -')
print(sess.run(matrix_A))
print('- - - - - - - - - - - - - - - - - - - -')
print(sess.run(matrix_B))
print('- - - - - - - - - - - - - - - - - - - -')
print(sess.run(matrix_C))
print('- - - - - - - - - - - - - - - - - - - -')
print(sess.run(matrix_D))

# 若再次运行sess.run(matrix_D)
# Tensorflow会重新初始化变量
# 会得到不同的随机数

# 2.矩阵加法与减法


print('- - - - - - - - - - - - - - - - - - - -')
print(sess.run(matrix_A+matrix_B))
print('- - - - - - - - - - - - - - - - - - - -')
print(sess.run(matrix_A-matrix_B))
print('- - - - - - - - - - - - - - - - - - - -')

# 矩阵乘法
print(sess.run(tf.matmul(matrix_B,indentity_matrix)))
# 矩阵乘法注意矩阵前后次序，以及对应的阶次

print('- - - - - - - - - - - - - - - - - - - -')
# 矩阵转置
print(sess.run(tf.transpose(matrix_C)))
# 重新初始化会得到不同的值，
# 所以会与之前的matrix_C不是转置矩阵

print('- - - - - - - - - - - - - - - - - - - -')
# 矩阵行列式
print(sess.run(tf.matrix_determinant(matrix_D)))

print('- - - - - - - - - - - - - - - - - - - -')
# 矩阵的逆矩阵
print(sess.run(tf.matrix_inverse(matrix_D)))
# 矩阵的逆矩阵是用平方根法，
# 需要矩阵为对称正定矩阵或者可进行LU分解

print('- - - - - - - - - - - - - - - - - - - -')
# 矩阵分解法
print(sess.run(tf.cholesky(indentity_matrix)))

print('- - - - - - - - - - - - - - - - - - - -')
# 求矩阵特征值和特征向量
print(sess.run(tf.self_adjoint_eig(matrix_D)))
# 第一行 为特征值，
# 其余的向量是对应的特征向量
# 此方法又称矩阵的特征分解





