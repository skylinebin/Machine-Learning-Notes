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