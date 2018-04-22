'''
一.分析数据
二.缺失值处理
三.异常值处理
四.去重处理
五.噪音数据处理
六.一些实用的数据处理小工具
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

if __name__=='__main__':
    # 一组年薪超过10万元的经理收入
    pay=np.array([11,19,14,22,14,28,13,81,12,43,11,16,
                  31,16,23.42,22,26,17,22,13,27,180,16,
                  43,82,14,11,51,76,28,66,29,14,14,65,
                  37,16,37,35,39,27,14,17,13,38,28,40,
                  85,32,25,26,16,12,54,40,18,27,16,14,
                  33,29,77,50,19,34])
    plt.subplot(2,2,1)#将绘图窗口改成2*2，可同时显示四幅图
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    plt.subplot(2, 2, 2)
    plt.plot(pay)
    plt.subplot(2, 2, 3)
   # plt.show()
    #二.缺失值处理
    data = sp.genfromtxt("../data_analyze/data_analyze.py", delimiter="\t")#读出来是numpy数组
    data = pd.read_table("../data_analyze/web_traffic.tsv", header=None, names=['A','B'])#
    #读出来是dataframe的格式，每一列每一行都是Series的格式，如果列没有抬头，就用这种方式
    print("data shape 为{}".format(data.shape))
    x = data.A
    y = data.B
    queshi_y = sp.sum(sp.isnan(y))#缺失值的数量,isnan()会对该数值是否为nan返回一个布尔值
    queshi_x = sp.sum(sp.isnan(x))
    print("x的缺失值数量为{},y的缺失值数量为{}".format(queshi_x,queshi_y))
    
    #三、异常值处理
    print(data.describe())
    data1 = data.fillna(0)#补零
    x1 = data1.A
    y1 = data1.B
    queshi_y = sp.sum(sp.isnan(y1))#缺失值的数量,isnan()会对该数值是否为nan返回一个布尔值
    queshi_x = sp.sum(sp.isnan(x1))
    print("x的缺失值数量为{},y的缺失值数量为{}".format(queshi_x,queshi_y))
    print(data1.describe())

    data1 = data.dropna()#丢弃
    x1 = data1.A
    y1 = data1.B
    queshi_y = sp.sum(sp.isnan(y1))#缺失值的数量,isnan()会对该数值是否为nan返回一个布尔值
    queshi_x = sp.sum(sp.isnan(x1))
    print("x的缺失值数量为{},y的缺失值数量为{}".format(queshi_x,queshi_y))
    print(data1.describe())
    print(data1)


