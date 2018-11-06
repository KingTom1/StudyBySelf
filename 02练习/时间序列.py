import pandas as pd
import numpy as np
from numpy.random import randn
from datetime import datetime
now= datetime.now()
print(now)
print(now.year)
t=datetime(2017,1,2,1,21,30)-datetime(2016,2,3)
print(t)
#字符串和datetime的相互转换
print(str(now))
value='2011-03-10'
print(datetime.strptime(value,'%Y-%m-%d'))
#时间索引
l_ts=pd.Series(randn(1000),index=pd.date_range('1/1/2010',periods=1000))
print(l_ts)
print(l_ts.dtypes)
# print(l_ts['2011'])
# print(l_ts['2011-03'])
# print(l_ts['1/2/2010':'1/3/2010'])
# print(l_ts['2010-01-31':'2010-02-02'])
# print(l_ts.truncate(after='1/3/2010'))
# dates=pd.date_range('2010-01-01',periods=100,freq='W-WED')
# df=pd.DataFrame(randn(100,4),index=dates,columns=['A','B','C','D'])
# print(df)
# print(df.ix['2011-03'])
#日期的范围、频率、移动
ts=pd.Series(randn(100),index=pd.date_range('1/1/2010',periods=100,freq='W-WED'))
print(ts)
print(ts.resample('D'))
index=pd.date_range('2010-01','2010-03',freq='M')
print(index.month)
# pandas中的频率是由一个基础频率和一个乘数组成。
# 基础频率通常是一个字符串别名表示，如“M”表示每月，“H”表示每小时
# 对每个基础频率都有一个偏移量的对象与之对应。
# D Day 日
# B BusinessDay 工作日
# H Hour 每小时
# T或min Minute 每分
# S Second 每秒
# L或ms Milli 每毫秒
# M MonthEnd 每月最后一天
# BM BusinessMonthEnd 每月最后一个工作日
# MS MonthBegin 每月第一个天
# BMS BusinessMonthBegin 每月第一个工作日
# W-MON.. Week 从指定星期几【MON、TUE、WED、THU、FRI、SAT、SUN】开始算起，每周
# WOM-1MON、WOM-2MON.. WeekofMonth 产生每月第1、第2..周星期几
# Q-JAN、Q-FEB.. QuarterEnd 对于指定月份【JAN、FEB、MAR、APR、MAY、JUN、JUL、AUG、SEP、OCT、NOV、DES】结束年度，每季度最后一月的最后一天
# BQ-JAN BusinessQuarterEnd 每季度最后一月的最后一个工作日
# QS-JAN QuanterBegin 每季度最后一月的第一个天
# BQS-JAN BusinessQuanterBegin 每季度最后一月的第一个工作日
# A-JAN YearEnd 每年指定月份最后一天
# BA-JAN BusinessYearEnd 每年指定月份最后一个工作日
# AS-JAN YearBegin 每年指定月份第一天
# BAS-JAN BusinessYearBegin 每年指定月份第一个工作日
print(pd.date_range('2010-01-01',periods=10,freq='1h20min30s'))
print(pd.date_range('2010-01-01',periods=10,freq='MS'))
print(pd.date_range('2010-01-01',periods=10,freq='M'))
print(pd.date_range('2010-01-01',periods=10,freq='BQ-JAN'))
print(pd.date_range('2010-01-01',periods=10,freq='WOM-1MON'))
# 移动数据 移动【Shifting】是指沿着时间轴将数据前移或后移。
# Series和DataFrame都有一个Shift方法用于单纯的前移和后移操作。
data=[1,2,3,4,5]
ts=pd.Series(data,index=pd.date_range('2010-01-01',periods=5,freq='M'))
print(ts)
print(ts.shift(1))
print(ts.shift(-2))
print(ts/ts.shift(1)+1)
# 时期以及算数运算
# 时期【Period】表示的是时间区间，比如数日、数月、数季、数年等。
print(pd.period_range('2010-01-01','2010-12-12',freq='M'))
# 时期频率转换
# Period和PeriodIndex对象都可以通过其asfreq方法被转化成别的频率。
p=pd.period_range('2010-01-01','2010-12-12',freq='M')
print(p.asfreq('D',how='Start'))
# Timestamp与Period转换
# 通过to_period方法由时间戳索引的Series和DataFrame对象转换成以时期索引
rng=pd.period_range('2010-01-01',periods=3,freq='M')
ts=pd.Series(randn(len(rng)),index=rng)
print(ts)