''' coding: utf-8 '''

import tensorflow as tf

import numpy as np


#生成一些数据
x_data = np.random.rand(100).astype(np.float32)

y_data = x_data*0.1 + 0.3

# start the structure of tensorflow

#生成tensorflow　结构
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))#随即生成参数
biases = tf.Variable(tf.zeros([1]))#初始值为０

#从初始值不断提升

y = Weights*x_data + biases
#提升y的准确度

loss = tf.reduce_mean(tf.square(y - y_data))

#选择学习效率
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

# init = tf.global_variables_initializer() #新的写法

# end the structure of tensorflow

sess = tf.Session()
sess.run(init)#激活init Very important

for step in range(201):
	sess.run(train)
	if(step % 20 == 0):
		print(step,sess.run(Weights),sess.run(biases))
