import tensorflow as tf
import numpy as np

row_dim = 10
col_dim = 10

# 1.固定张量

#创建固定维度的零张量
zero_tsr =tf.zeros([row_dim,col_dim])

#创建指定维度的单位张量
ones_tsr =tf.ones([row_dim,col_dim])

#创建指定维度的常数填充张量
filled_tsr = tf.fill([row_dim,col_dim], 42)

#使用已知常数张量创建张量
constant_tsr = tf.constant([1,2,3])

# 2.相似张量

# 新建与已有张量类似的张量
zero_similar = tf.zeros_like(constant_tsr)
ones_similar = tf.ones_like(constant_tsr)

# 3.序列张量

# 创建指定间隔的张量,包括结尾值
linear_tsr = tf.linspace(start=0.0,stop=1.0,num=7)
# when num=7, output is  [0.         0.16666667 0.33333334 0.5        0.6666667  0.8333334 1.        ]

# 随机取间隔递增值不包括结尾值
integer_seq_tsr = tf.range(start=6,limit=20,delta=3)
# when start=6,limit=20, delta =3, output is [ 6  9 12 15 18]

# 4.随机张量

# 生成均匀分布的随机数
randunif_tsr = tf.random_uniform([row_dim,col_dim], minval=0, maxval=2)
# when maxval=2, one row is [1.4330745  1.6743479  1.4814448  0.16386724 1.9783459  1.0236795
#   0.1930139  0.34939528 1.3543162  0.4354465 ]
# in this function, minval <= x < maxval

# 生成正态分布的随机数
randnorm_tsr = tf.random_normal([row_dim,col_dim], mean=0.0, stddev=1.0)

# 生成随机数位于指定期望到两个标准差之间的区间
runcnorm_tsr = tf.truncated_normal([row_dim,col_dim], mean=0.0, stddev=1.0)


# 张量和数组随机化

# 随机调整张量参数的顺序
shuffled_output_tsr = tf.random_shuffle(constant_tsr)

oldconstant_tsr = tf.constant([[1,2,3],[4,5,6],[7,8,9]])


# 对原有张量进行随机裁剪
cropped_output_tsr = tf.random_crop(oldconstant_tsr,[3,1])
# 张量裁剪，要注意维数和通道数, 3*3 可被裁剪顶多是二维
# when size=[3,1], output is [[1] [4] [7]]

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(oldconstant_tsr))
print('- - - - - - - - - - - - - - - - - - - -')
print(sess.run(cropped_output_tsr))

writer = tf.summary.FileWriter('logs/',sess.graph)

# 创建好张量,使用tf.Variable()封装张量作为变量
print('- - - - - - - - - - - - - - - - - - - -')
first_zero_var = tf.Variable(zero_tsr)

# 也可使用 tf.convert_to_sensor()

initialize_option = tf.global_variables_initializer()
sess.run(initialize_option)
print('- - - - - - - - - - - - - - - - - - - -')
# 占位符形成
init_x = tf.placeholder(tf.float32, shape=[2,2])
# 占位符要声明数据格式
init_y = tf.identity(init_x)
x_vals = np.random.rand(2,2)
sess.run(init_y, feed_dict={init_x: x_vals})
# print(init_y)