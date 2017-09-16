''' coding: utf-8 '''

from __future__ import print_function
import tensorflow as tf

import numpy as np

# Show the function of Tensorboard secondly
#

# Create a full neural network
def add_layer(inputs,in_size,out_size,n_layer,activation_function=None):
    layer_name = 'layer%s' % n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='W')
            tf.summary.histogram(layer_name + '/weights',Weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1,out_size])+0.1,name='b')
            tf.summary.histogram(layer_name + '/biases',biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.add(tf.matmul(inputs,Weights),biases)
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name + '/outputs',outputs)
    return outputs

# Makeup some datas
x_data = np.linspace(-1,1,300,dtype=np.float32)[:,np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape).astype(np.float32)
y_data = np.square(x_data)-0.5+noise


with tf.name_scope('inputs'):
    #Define placeholder for inputs to network
    xs = tf.placeholder(tf.float32,[None,1],name='x_input')
    ys = tf.placeholder(tf.float32,[None,1],name='y_input')

# Create 1 input_layer and 10 hidden_layer and 1 output_layer

# Define hidden layer
layer1 = add_layer(xs,1,10,n_layer=1,activation_function=tf.nn.relu)
# tf.nn.relu is the activatonfunc of Tensorflow

#Define output layer
prediction = add_layer(layer1,10,1,n_layer=2,activation_function=None)

# Calculate the deviation betwween the prediction and real value
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))
    tf.summary.scalar('loss', loss)

# machine involve the accuracy rate
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)


# init the variable of tf
# init = tf.global_variables_initializer()

# Define Session to init
sess = tf.Session()
merged = tf.summary.merge_all()
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
for i in range(1000):
    sess.run(train_step, feed_dict={xs:x_data,ys:y_data})
    if i % 50 == 0:
        result = sess.run(merged,feed_dict={xs:x_data,ys:y_data})
        writer.add_summary(result, i)
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))