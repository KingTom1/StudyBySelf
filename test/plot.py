# # 导入模块
# import matplotlib.pyplot as plt
#
# # 数据
# squares = [1,4,9,16,25]
#
# # 绘制图形: 曲线图
# # plt.plot(squares)
# # 绘制图形
# # plt.show()
#
# # 绘制    散点图
# # x 轴
# x = list(range(6))
# # y 轴
# y = [1,4,9,16,25]
# plt.scatter(x,y)
# plt.show()

import pyodbc
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.22.134.200;DATABASE=指标集管理系统;UID=sa;PWD=P@ssw0rd')
# #cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=test;UID=sa;PWD=bi.123456')
# #cnxn = pyodbc.connect('172.22.134.200','指标集管理系统','sa','P@ssw0rd')
# #pyodbc.connect('172.22.134.200','指标集管理系统','sa','P@ssw0rd')
# cursor = cnxn.cursor()
# cursor.execute("select DISTINCT Loc8DR from KPI竖表 ")
# # sql = 'select * from 统计项定义'
# # cursor.execute(sql)
# #用一个rs变量获取数据
# rs = cursor.fetchall()
# print(rs)

import numpy as np
# to_forecast=np.arange(6)
# print(to_forecast)
# window=3
# shape = to_forecast.shape[:-1] + (to_forecast.shape[-1] - window + 1, window)
# print(to_forecast.shape[:-1])
# print(to_forecast.shape[-1])
# print(shape)
#
# b = [[1,2,3],[4,5,6],[7,8,9]]
# print(np.shape(b))
# print(np.array(b).shape)
# print(to_forecast[:-1])
# print(b[:-1])
# print(b[:-1],to_forecast)

from pandas.tseries.offsets import *
import logging
X1 = [1,2,3,4,5]
X = [[1,2],[3,4]]
y = 1
dates = 1
res = np.arange(5)
period = 7
window = 1
def predict(X1,X,y,dates,res,period,window):
    print('进入方法')
    pre2 = res.predict(X1)
    X1 = np.append(X1,pre2)

    if period == 1:
        X2 = X1[1:(window+1)]
        X = np.vstack((X,X2))
        y = np.append(y,pre2)
        dates1 = dates[(len(dates)-1):]+Day(1)
    elif period == 2:
        X2 = X1[1:(window+1)]
        X = np.vstack((X,X2))
        y = np.append(y,pre2)
        dates1 = dates[(len(dates)-1):]+ DateOffset(months=1)
    else:
        logging.debug('ERROR in predict')

    dates = dates.append(dates1)

    print(X2,X,y,dates)
    return X2,X,y,dates

predict(X1,X,y,dates,res,period,window)