# Tensorflow基础介绍


## in tensorlearning.py

### 1.Tensorflow中张量的形成

### 2.Tensorflow中变量与占位符的区别

使用 tensorboard 可视化网络图谱

```python
writer = tf.summary.FileWriter('logs/',sess.graph)

```

在Terminal中输入
```
tensorboard --logdir logs

```
可以在浏览器查看网络情况



## in tensormatrix.py

### 1.创建矩阵及其相关操作

### 2.矩阵加法与减法

### 3.矩阵操作,逆矩阵，转置矩阵，求特征值和特征向量


## in tensormathfunc.py

### 记录了tensorflow中的数学函数的使用方法



## in tensoractivation.py

### 详细分析了tensorflow中常用激励函数类型以及对应的原理
sigmoidFunction.png & sigmoidFunction2.png 展示了激励函数之间的对比情况


## in tensordatasource.py
### 实践了tensorflow中调用和处理数据源的操作方法
版本出现调整可能导致部分读取数据源方法出现错误


## in MachineLearningOne.py  MachineLearningTwo.py 
### 计算图中不同层级的联接 

## in MachineLearningThree.py 
### 使用 Tensorflow 实现各种损失函数



