# -*- coding:utf-8 -*-

import tensorflow as tf


sess = tf.Session()


print(sess.run(tf.div(3,4)))
# div函数返回值的数据类型与输入数据类型一致
print('- - - - - - - - - - - - - - - - - - - -')
print(sess.run(tf.truediv(3,4)))
# 在python3中,使用truediv在整数相除之前都转换成浮点数进行运算

# 对浮点数进行整数除法
print('- - - - - - - - - - - - - - - - - - - -')
print(sess.run(tf.floordiv(3.0,4.0)))
# 取整操作,返回浮点数，但舍去小数位

# 取模操作
print('- - - - - - - - - - - - - - - - - - - -')
print(sess.run(tf.mod(22.0,5.0)))
# 返回除法的余数，自然为浮点数

# 计算两张量间的点积
print('- - - - - - - - - - - - - - - - - - - -')
print(sess.run(tf.cross([1.,0.,0.],[0.,1., 0.])))
# 点积只为三维向量定义

# 数学函数列表中还有:
# abs(),ceil(),cos(),exp(),floor(),inv(),log(),
# maximum(),minimum(),neg(),pow(),round(),
# rsqrt(),sign(),sin(),sqrt()张量的平方根,square()张量的平方


# 特殊数学函数
# tf.digamma() Psi函数, lgamma()函数的导数
# tf.erf() 张量的高斯误差函数
# tf.erfc() 张量的互补误差函数
# tf.igamma() 下不完全伽马函数
# tf.igammac() 上不完全伽马函数
# tf.lbeta() 贝塔函数绝对值的自然对数
# tf.lgamma() 伽马函数绝对值的自然对数
# tf.squared_difference() 两个张量间差值的平方

