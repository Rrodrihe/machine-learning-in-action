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

# k-近邻算法(2.1 k-近邻算法概述)
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
    # 排序(按字典的value倒序排列)
    '''
    sortedClassCount = [('B', 2), ('A', 1)]
    '''
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0] 

# 数据准备(2.1 k-近邻算法概述)
def createDataSet():
    # 二维数组
    # 这里有平面上的四个点，这里指定了他们的平面坐标(两个特征/属性)
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    # 这里的四个值对应四个点的类别(目标变量)
    labels = ['A', 'A', 'B', 'B']
    return group, labels

# 读取文件并将其内容转换成矩阵(2.2 示例：使用k-近邻算法改进约会网站的配对效果)
def file2matrix(filename):
    love_dictionary = {'largeDoses': 3, 'smallDoses': 2, 'didntLike': 1}
    # 打开文件
    fr = open(filename)
    # 将文件内容读出来存入list, 每一行作为一个元素
    arrayOLines = fr.readlines()
    # 获取文件行数，即：list的长度(list的元素个数)
    numberOfLines = len(arrayOLines)
    # [返回值]创建一个元素值全为0的N*3数组
    returnMat = zeros((numberOfLines, 3))
    # [返回值]创建一个空list
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        # 去除字符串首尾空白字符
        line = line.strip()
        # 拆分字符串，将各字段存入list
        listFromLine = line.split('\t')



