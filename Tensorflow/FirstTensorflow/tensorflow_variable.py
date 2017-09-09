''' coding: utf-8 '''

import tensorflow as tf

import numpy as np

state = tf.Variable(0,name='counter') #定义变量

# print(state.name)

one = tf.constant(1)

new_value = tf.add(state, one)
update = tf.assign(state,new_value)

init = tf.initialize_all_variables() # must have if define variable

with tf.Session() as sess:
	sess.run(init)
	for _ in range(3):
		sess.run(update)
		print(sess.run(state))