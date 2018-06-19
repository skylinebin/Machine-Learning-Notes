# -*- coding:utf-8 -*-

import tensorflow as tf

import requests

# 1.Datasets One (Iris data)
print('- - - - - - - -Iris data - - - - - - - - - -')
from sklearn import datasets
# python -m pip install sklearn


iris = datasets.load_iris()

print(len(iris.data))
print(len(iris.target))
print(iris.data[0])
# output is [5.1 3.5 1.4 0.2]

print(set(iris.target))
# output is {0, 1, 2}




# 2.Datasets Two (Boston Housing data)
print('- - - - - - - -housing.data - - - - - - - - - -')
# housing_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing_header = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV0']
housing_file = open('./housing.data')
housingdatas = housing_file.read()
housing_data = [[float(x) for x in y.split(' ') if len(x)>=1] for y in housingdatas.split('\n') if len(y)>=1]
# 换成读取本地数据,调整读取数据形式
print(len(housing_data))
# output is 506
print(len(housing_data[0]))
# output is 14

# 3.Datasets Three
# print('- - - - - - - -MNIST_data - - - - - - - - - -')
# this version of codes is outdate

# from tensorflow.examples.tutorials.mnist import input_data
# mnist = input_data.read_data_sets('MNIST_data','one_hot=True')
# # mnist = input_data.absolute_import('MNIST_data','one_hot=True')
# print(len(mnist.train.images))
# print(len(mnist.test.images))
# print(len(mnist.validation.images))
# print(mnist.train.images[1,:])



# 4.Datasets Four (Shakespeare)
print('- - - - - - - -Shakespeare - - - - - - - - - -')
shakespeare_file = open('./100-0.txt','r', encoding='UTF-8').read()
# shakespeare_file = open('./100-0.txt', 'rb').read()
# Decode binary into string
# shakespeare_text = shakespeare_file.decode('utf-8')
shakespeare_text = shakespeare_file

# Drop first few descriptive paragraphs.
shakespeare_text = shakespeare_text[7675:]
print(len(shakespeare_text))

# 5.Datasets Five (Deu-Eng)
print('- - - - - - - -Deu-Eng - - - - - - - - - -')
file = open('deu.txt','r', encoding='UTF-8').read()
# Format Data
eng_ger_data = file
eng_ger_data = eng_ger_data.encode('ascii''',errors='ignore''')
eng_ger_data = eng_ger_data.decode().split('\n')
eng_ger_data = [x.split('\t') for x in eng_ger_data if len(x)>=1 ]
[english_sentence, german_sentence] = [list(x) for x in zip(*eng_ger_data)]
print(len(english_sentence))
print(len(german_sentence))
print(eng_ger_data[10])