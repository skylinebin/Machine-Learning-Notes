''' coding: utf-8 '''

from __future__ import print_function
import tensorflow as tf


# Show the function of Tensorboard
#

# Create a full neural network
def add_layer(inputs,in_size,out_size,activation_function=None):
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='W')
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1,out_size])+0.1,name='b')
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.add(tf.matmul(inputs,Weights),biases)
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs

with tf.name_scope('inputs'):
    #Define placeholder for inputs to network
    xs = tf.placeholder(tf.float32,[None,1],name='x_input')
    ys = tf.placeholder(tf.float32,[None,1],name='y_input')

# Create 1 input_layer and 10 hidden_layer and 1 output_layer

# Define hidden layer
layer1 = add_layer(xs,1,10,activation_function=tf.nn.relu)
# tf.nn.relu is the activatonfunc of Tensorflow

#Define output layer
prediction = add_layer(layer1,10,1,activation_function=None)

# Calculate the deviation betwween the prediction and real value
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))

# machine involve the accuracy rate
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)


# init the variable of tf
# init = tf.global_variables_initializer()

# Define Session to init
sess = tf.Session()
# sess.run(init)

# Check the version of Tensorflow, and output the logs
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    writer = tf.train.SummaryWriter('logs/',sess.graph)
else:
    writer = tf.summary.FileWriter('logs/',sess.graph)


# Check the version of Tensorflow, and init the variables
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    init = tf.initialize_all_variables()
else:
    init = tf.global_variables_initializer()

sess.run(init)

# Use : tensorboard --logdir logs

# Start Learning
# for i in range(1000):
# 	# training
# 	sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
#
# 	if i % 50 ==0:
# 		# print the step improvement
# 		print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))