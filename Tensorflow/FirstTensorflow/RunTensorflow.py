import tensorflow as tf

row_dim = 10
col_dim = 10

#创建固定维度的零张量
zero_tsr =tf.zeros([row_dim,col_dim])

#创建指定维度的单位张量
ones_tsr =tf.ones([row_dim,col_dim])

#创建指定维度的常数填充张量
filled_tsr = tf.fill([row_dim,col_dim], 42)


hello = tf.constant(b'Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))