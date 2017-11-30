''' coding: utf-8 '''
from __future__ import print_function
# 如果不加上上面这一句，会出现连接断开的错误
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)
# 下载

sess = tf.InteractiveSession()
#注册一个默认的session

x = tf.placeholder(tf.float32, [None, 784])
#数据输入接口，None表示条数不受限制，784表示每一条均为784维的数据

W = tf.Variable(tf.zeros([784,10]))
#Weights 的shape是[784,10],784是特征的维数，而后面的10代表有10类
b = tf.Variable(tf.zeros([10]))
#Biases 10类对应的偏量值

y = tf.nn.softmax(tf.matmul(x,W) + b)
#执行 Softmax Regression 算法的公式

y_ = tf.placeholder(tf.float32, [None,10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y), reduction_indices=[1]))
#定义损失函数

#定义优化算法来准备开始训练
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

#使用全局参数初始化器指令run方法
sess.run(tf.global_variables_initializer())

#开始迭代执行训练操作 train_ste

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    train_step.run({x: batch_xs, y_: batch_ys})

#评测准确率
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(accuracy.eval({x:mnist.test.images, y_: mnist.test.labels}))