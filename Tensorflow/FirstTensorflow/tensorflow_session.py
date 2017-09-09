''' coding: utf-8 '''

import tensorflow as tf

import numpy as np

matrix_1 = tf.constant([[3,3]])
matrix_2 = tf.constant([[3],[2]])

product = tf.matmul(matrix_1,matrix_2)#矩阵相乘 dot(m1,m2)

#mothod1
# sess = tf.Session()

# result = sess.run(product)
# print(result)
# sess.close()

#method2
with tf.Session() as sess:
	result2 = sess.run(product)
	print(result2)

	
