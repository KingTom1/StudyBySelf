###########################Series 学习###################################
# Series 一种类似于一位数组的对象，它由一组数据以及一组与之相关的数据标签（即索引）组成

from pandas import Series,DataFrame
import pandas as pd

s = Series([1,2,3.0,'abc'])
s2 = Series(['a','v','c'])
# print('获取数据',s)
# print('第一个数据',s[0])
# s[3]='liusen'
# print('更新后的数据',s)
# del s[3]
# print('删除最后一行数据',s)

series = pd.Series(s.ix[len(s)-1], index=s2.index)
print(series)