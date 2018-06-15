# -*- coding:utf-8 -*-

import tensorflow as tf
import numpy as np
import matplotlib.pylab as plt

sess = tf.Session()


# 自定义函数

def custom_polynomial(value):
    return (tf.subtract(3 * tf.square(value), value)+10)

print(sess.run(custom_polynomial(11)))

# 激励函数

print('- - - - - - - -relu - - - - - - - - - -')
# 1.ReLU 整流线型单元 relu激励函数
print(sess.run(tf.nn.relu([-3., 3., 10.])))
# output is [ 0.  3. 10.] same as max(0,x)

print('- - - - - - - relu6 - - - - - - - - - - -')
print(sess.run(tf.nn.relu6([-3., 3., 10.])))
# output is [0. 3. 6.] same as min(max(0, x), 6)

# 2.逻辑函数 sigmoid激励函数
print('- - - - - - sigmoid - - - - - - - - - - -')
print(sess.run(tf.nn.sigmoid([-1., 0., 1.])))
# output is [0.26894143 0.5        0.7310586 ]
# same as 1/(1 + exp(-x))   1/(1+exp(-1)) = 0.731058578630005 from matlab
# 取值0~1

# 3.双曲正切函数 tanh 激励函数
print('- - - - - - - tanh- - - - - - - - - - -')
print(sess.run(tf.nn.tanh([-1., 0., 1.])))
# output is [-0.7615942  0.         0.7615942]
# same as (exp(x) - exp(-x))/(exp(x) + exp(-x))
# 取值范围为-1~1

# 4.softsign激励函数
print('- - - - - - - softsign - - - - - - - - - - -')
print(sess.run(tf.nn.softsign([-1., 0., -1.])))
# output is [-0.5  0.  -0.5]
# same as x/(abs(x) + 1)

# 5.softplus激励函数
print('- - - - - - - softplus - - - - - - - - - - -')
print(sess.run(tf.nn.softplus([-1., 0., -1.])))
# output is [0.31326166 0.6931472  0.31326166]
# same as log(exp(x) + 1)

# 6.ELU激励函数
print('- - - - - - - elu - - - - - - - - - - -')
print(sess.run(tf.nn.elu([-1., 0., 1.])))
# output is [-0.63212055  0.          1.        ]
# same as x<0? (exp(x)+1):x


x = np.linspace(-10.0, 10.0)
plt.figure(1)

plt.plot(x , sess.run(tf.nn.relu(x)), label='relu')
plt.plot(x , sess.run(tf.nn.relu6(x)), label='relu6')
plt.plot(x , sess.run(tf.nn.softplus(x)), label='softplus')
plt.plot(x , sess.run(tf.nn.elu(x)), label='elu')

plt.legend()
plt.show()

plt.figure(2)
plt.plot(x , sess.run(tf.nn.softsign(x)), label='softsign')
plt.plot(x , sess.run(tf.nn.sigmoid(x)), label='sigmoid')
plt.plot(x , sess.run(tf.nn.tanh(x)), label='tanh')

plt.legend()
plt.show()
