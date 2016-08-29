# -*- coding: utf-8 -*-

'''
/***********************************************************
      FileName: kNN.py
          Desc: k近邻算法(k Nearest Neighbors)
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2016-08-29 16:18:04
       History:
 ***********************************************************/
'''

from numpy import *
import operator

# k-近邻算法
'''
输入
inX: 待定样本
dataSet: 训练集(数据样本集合)
labels: 训练集各样本对应的标签
k: 近邻数量(通常不大于20)
'''
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]


# 数据准备
def createDataSet():
    # Q: 数组元素为什么是个列表
    # 这里有平面上的四个点，这里指定了他们的平面坐标(两个特征/属性)
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    # 这里的四个值对应四个点的类别(目标变量)
    labels = ['A', 'A', 'B', 'B']
    return group, labels


