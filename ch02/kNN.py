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
    # 距离计算(平方和开根)
    ## 获取二维数组的行数, 示例：dataSet.shape = (4, 2)
    dataSetSize = dataSet.shape[0]  # 4
    ## 计算inX到数据集合中各点的距离
    '''
    diffMat = array([[-1. , -1.1],
                     [-1. , -1. ],
                     [ 0. ,  0. ],
                     [ 0. , -0.1]])
    '''
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    ## 平方
    '''
    sqDiffMat = array([[ 1.  ,  1.21],
                       [ 1.  ,  1.  ],
                       [ 0.  ,  0.  ],
                       [ 0.  ,  0.01]])
    '''
    sqDiffMat = diffMat ** 2
    ## 平方和
    ## sum函数参考: http://scipy.github.io/old-wiki/pages/Numpy_Example_List.html#sum.28.29
    '''
    sqDistances = array([ 2.21,  2.  ,  0.  ,  0.01])
    '''
    sqDistances = sqDiffMat.sum(axis = 1)
    ## 平方和开根
    '''
    distances = array([ 1.48660687,  1.41421356,  0.        ,  0.1       ])
    '''
    distances = sqDistances ** 0.5
    ## argsort函数：http://scipy.github.io/old-wiki/pages/Numpy_Example_List.html#argsort.28.29
    ## 按从小到大排序，argsort返回排序后各元素对应的下标
    '''
    sortedDistIndicies = array([2, 3, 1, 0])
    '''
    sortedDistIndicies = distances.argsort()
    # 选择距离最小的k个点
    ## 使用dict类型保存数据
    classCount = {}
    ## range用于生成整数列表 
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        '''
        ## 第1次处理结束时：classCount = {'B': 1}
        ## 第k次处理结束时：classCount = {'A': 1, 'B': 2}
        '''
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 
    # 排序
    '''
    sortedClassCount = [('B', 2), ('A', 1)]
    '''
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0] 

# 数据准备
def createDataSet():
    # 二维数组
    # 这里有平面上的四个点，这里指定了他们的平面坐标(两个特征/属性)
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    # 这里的四个值对应四个点的类别(目标变量)
    labels = ['A', 'A', 'B', 'B']
    return group, labels

