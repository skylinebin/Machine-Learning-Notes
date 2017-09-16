''' coding: utf-8 '''



from __future__ import print_function
import tensorflow as tf

import numpy as np

learning_rate = 0.5
tf.train.GradientDescentOptimizer.__init__(learning_rate,use_locking=False,name='GradientDescent')
