''' coding: utf-8 '''

from __future__ import print_function
import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt

# Create a full neural network
def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size])+0.1)

    Wx_plus_b = tf.matmul(inputs,Weights)+biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

# Create some datas
x_data = np.linspace(-1,1,300,dtype=np.float32)[:,np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape).astype(np.float32)
y_data = np.square(x_data)-0.5+noise

# Define the input of neural network
xs = tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])

# Create 1 input_layer and 10 hidden_layer and 1 output_layer

# Define hidden layer
layer1 = add_layer(xs,1,10,activation_function=tf.nn.relu)
# tf.nn.relu is the activatonfunc of Tensorflow

#Define output layer
prediction = add_layer(layer1,10,1,activation_function=None)

# Calculate the deviation betwween the prediction and real value
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))

# machine involve the accuracy rate
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# prapare to init variable
sess = tf.Session()

if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
	init = tf.initialize_all_variables()
else:
	init = tf.global_variables_initializer()
sess.run(init)

# plot the real data in a figure
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()
plt.show()

# Start Learning 
for i in range(1000):
	sess.run(train_step, feed_dict={xs:x_data,ys:y_data})

	if i % 50 == 0:
		# to visualize the result and improment
		try:
			ax.lines.remove(lines[0])
		except Exception:
			pass
		prediction_value = sess.run(prediction, feed_dict={xs:x_data})
		# plot the prediction
		lines = ax.plot(x_data, prediction_value, 'r-',lw=5)
		plt.pause(1)
