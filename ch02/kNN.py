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

# 导入matplotlib用于生成图形
import matplotlib
matplotlib.use('Agg')  # 该条语句必须在import matplotlib之后
import matplotlib.pyplot as plt


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
        # 将每行的前三个字段存入矩阵二维数组
        '''
        returnMat = array([[  4.09200000e+04,   8.32697600e+00,   9.53952000e-01],
                           [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00],
                           ...])
        '''
        # returnMat[index,:]表示编号为index的这一行上的所有元素(应该是一个list)
        returnMat[index,:] = listFromLine[0:3]
        # 将每行的第四个字段存入classLabelVector
        if (listFromLine[-1].isdigit()):
            classLabelVector.append(int(listFromLine[-1])) 
        else:
            classLabelVector.append(love_dictionary.get(listFromLine[-1])) 
        index += 1
    return returnMat, classLabelVector
        
# 使用Matplotlib(2.2 示例：使用k-近邻算法改进约会网站的配对效果)
def drawScatter1():
    # 获取矩阵和标签
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt') 
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 使用第2个和第3个特征(玩视频游戏所耗时间百分比 & 每周消费的冰淇淋公升数)
    ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
    plt.savefig('images/scatter1.png', format='png')

# 使用Matplotlib(2.2 示例：使用k-近邻算法改进约会网站的配对效果)
# 与drawScatter1相比，使用不同的色彩和尺寸标记不同的类别
def drawScatter2():
    # 获取矩阵和标签
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt') 
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 使用第2个和第3个特征(玩视频游戏所耗时间百分比 & 每周消费的冰淇淋公升数)
    ax.scatter(datingDataMat[:,1], datingDataMat[:,2], (15.0 * array(datingLabels)), (15.0 * array(datingLabels)))
    plt.savefig('images/scatter2.png', format='png')

# 使用Matplotlib(2.2 示例：使用k-近邻算法改进约会网站的配对效果)
# 与drawScatter2相比，使用第1个特征和第2个特征(每年获得的飞行常客里程数 & 玩视频游戏所耗时间百分比)
def drawScatter3():
    # 获取矩阵和标签
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt') 
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 使用第1个特征和第2个特征(每年获得的飞行常客里程数 & 玩视频游戏所耗时间百分比)
    ax.scatter(datingDataMat[:,0], datingDataMat[:,1], (15.0 * array(datingLabels)), (15.0 * array(datingLabels)))
    plt.savefig('images/scatter3.png', format='png')

# 归一化特征值(2.2 示例：使用k-近邻算法改进约会网站的配对效果)
def autoNorm(dataSet):
    # 获取每一列的最小值，存入一维数组minVals
    minVals = dataSet.min(0)
    # 获取每一列的最大值，存入一维数组maxVals
    maxVals = dataSet.max(0)
    # 计算取值范围
    ranges = maxVals - minVals
    # 构建归一化数据集，和dataSet同等大小的二维数组, 这里：shape(dataSet) = (1000, 3)
    normDataSet = zeros(shape(dataSet))
    # 获取数据集的行数
    m = dataSet.shape[0]
    # 二维数组相减
    normDataSet = dataSet - tile(minVals, (m, 1))
    # 得到归一化数值，取值范围: [0-1]
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals
     
# 分类器针对约会网站的测试代码(2.2.4 测试算法：作为完整程序验证分类器) 
def datingClassTest():
    # 测试向量的比率(一般设置为0.1，即所有样本里，90%用于训练，10%用于测试)
    hoRatio = 0.50
    # 导入文件，转换成矩阵数组
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    # 特征值归一化处理
    normMat, ranges, minVals = autoNorm(datingDataMat)
    # 获取数据集的行数
    m = normMat.shape[0]
    # 测试向量个数(行数)
    numTestVecs= int(m * hoRatio)
    # 错误计数
    errorCount = 0.0
    # 遍历所有的测试向量，计算错误率
    for i in range(numTestVecs):
        # 调用kNN算法计算该条记录的分类
        # normMat[numTestVecs:m, :]表示测试向量后面的所有向量(训练向量，用于训练分类器)
        # datingLabels[numTestVecs:m]表示训练向量对应的类别(list类型)
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print "the classifire came back widh: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        # 判断kNN算法计算得到的分类和实际的分类是否相同
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print "the total error rate is: %f" % (errorCount / float(numTestVecs))
    print errorCount

