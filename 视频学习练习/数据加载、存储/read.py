import pandas as pd

a = pd.read_csv('ch06/ex2.csv', header=None)
print(a)

# a = pd.read_table('ch06/ex2.csv',sep=',')
# print(a)

b = pd.read_csv('ch06/ex2.csv', names=['a','b','c','d','message'])
print(b)

# 将某字段列作为索引的方式
names=['a','b','c','d','message']
c = pd.read_csv('ch06/ex2.csv',names=names,index_col='message')
print(c)

# 使用多列做层次化索引,index_col中顺序不能乱，第一个为第一层
parsed =  pd.read_csv("ch06/ex2.csv",names=names,index_col=['message','d'])
print(parsed)

# 将dataframe的数据写入csv文件
parsed.to_csv("ch06/out.csv")
