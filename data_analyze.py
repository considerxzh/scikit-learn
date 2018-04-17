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
    plt.bar(pay)
    plt.show()
    #二.缺失值处理
    data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")