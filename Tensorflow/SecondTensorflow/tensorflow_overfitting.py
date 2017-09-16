''' coding: utf-8 '''

from __future__ import print_function
import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

#
# Use dropout to solve overfitting problem
#

# Load datas
digits = load_digits()
X = digits.data
y = digits.target
y = LabelBinarizer().fit_transform(y)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.3)


# Create a full neural network
def add_layer(inputs,in_size,out_size,layer_name,activation_function=None,):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='W')
    tf.summary.histogram(layer_name + '/weights',Weights)
    biases = tf.Variable(tf.zeros([1,out_size])+0.1,)
    Wx_plus_b = tf.add(tf.matmul(inputs,Weights),biases)
    # to dropout
    Wx_plus_b = tf.nn.dropout(Wx_plus_b, keep_prob)
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b,)
    tf.summary.histogram(layer_name + '/outputs',outputs)
    return outputs


# define placeholder for inputs to Network
keep_prob = tf.placeholder(tf.float32)
xs = tf.placeholder(tf.float32,[None, 64]) # 8*8
ys = tf.placeholder(tf.float32,[None, 10]) # 8*8

# add output layer
# Define hidden layer
layer1 = add_layer(xs,64,50,'layerone',activation_function=tf.nn.tanh)
# tf.nn.relu is the activatonfunc of Tensorflow

#Define output layer
prediction = add_layer(layer1,50,10,'layertwo',activation_function=tf.nn.softmax)

# the error between prediction and data
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),reduction_indices=[1]))#loss
tf.summary.scalar('loss',cross_entropy)
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# Define Session to init
sess = tf.Session()
merged = tf.summary.merge_all()
# sess.run(init)

# Check the version of Tensorflow, and output the logs
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    train_writer = tf.train.SummaryWriter('logs/train',sess.graph)
    test_writer = tf.train.SummaryWriter('logs/test',sess.graph)
else:
    train_writer = tf.summary.FileWriter('logs/train',sess.graph)
    test_writer = tf.summary.FileWriter('logs/test',sess.graph)


# Check the version of Tensorflow, and init the variables
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    init = tf.initialize_all_variables()
else:
    init = tf.global_variables_initializer()

sess.run(init)

for i in range(500):
    sess.run(train_step,feed_dict={xs:X_train,ys:y_train,keep_prob:0.5})
    if i % 50 == 0:
        train_result = sess.run(merged,feed_dict={xs:X_train,ys:y_train,keep_prob:1})
        test_result = sess.run(merged,feed_dict={xs:X_test,ys:y_test,keep_prob:1})
        train_writer.add_summary(train_result,i)
        test_writer.add_summary(test_result,i)
#record loss






