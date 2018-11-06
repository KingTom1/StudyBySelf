###########################DataFrame 学习###################################
# DataFrame 一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型
# DataFrame中的数据是以一个或多个二位块存放的，不是列表、字典或别的一维数据结构
import pandas as pd
import numpy as np
#初始化方式1
df=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8],'w':[1,1,1,1],'s':[1,1,1,1]})
print(df)
#初始化方式2
s1=np.array([1,2,3,4])
s2=np.array([5,6,7,8])
df=pd.DataFrame([s1,s2])
print(df)
#初始化方式3
s3 = pd.Series([1,2,3.0,'abc'])
s4 = pd.Series([1,2,'mmmmm','abc'])
df = pd.DataFrame({"XXX1":s3,"XXX2":s4})
print(df)

df=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8],'w':[1,1,1,1],'s':[1,1,1,1]})

df.ix[df.A>1,'B']= -1    #修改某一列值
print(df)
del df['B']             #删除某一列

df2=df[0:]
print('df[0:]  -----------------')
print(df2)
print('df.iat[1,1]  --------------')
print(df.iat[1,1])     #选取第二行第二列，用于已知行、列位置的选取。
print('df.iloc[-1]   ------------------')
print(df.iloc[-1] )    #选取DataFrame最后一行，以列形式输出,返回的是Series
print('df.iloc[-1:]  -----------------')
print(df.iloc[-1:])    #选取DataFrame最后一行，以行形式输出,返回的是DataFrame
print('df[w] -----------------')
print(df['w'])         #选择表格中的'w'列，使用类字典属性,返回的是Series类型
print('df.w  -----------------')
print(df.w )           #选择表格中的'w'列，使用点属性,返回的是Series类型
print("df[['w']]  -----------------")
print(df[['w']])       #选择表格中的'w'列，返回的是DataFrame类型
print("df[['w','s']]  ---------------")
print(df[['w','s']])   #选择表格中的'w'、's'列
print('df[0:2]  -------------------')
print(df[0:2])         #返回第1行到第2行的所有行，前闭后开，包括前不包括后
print(df[1:2])         #返回第2行，从0计，返回的是单行，通过有前后值的索引形式
print(df.ix[1:2])      #返回第2行的第三种方法，返回的是DataFrame，跟data[1:2]同
print(df.head())       #返回data的前几行数据，默认为前五行，需要前十行则data.head(10)
print(df.tail())       #返回data的后几行数据，默认为后五行，需要后十行则data.tail(10)

#函数应用和映射
df=pd.DataFrame(np.random.randn(4,3),columns=list('bde'),index=['AAA','BBB','CCC','DDD'])
print(df.abs())
f = lambda x: x.max()-x.min()
print(df)
print(df.apply(f))
print(df.apply(f, axis=1))   #axis 行=0 列=1

#排序和排名
df=pd.DataFrame(np.arange(8).reshape((2,4)),index=['C','B'],columns=['a1','a3','a2','a4'])
print(df)
print('df.sort_index():::::::::::')
print(df.sort_index())
print('df.sort_index(axis=1):::::::::::::::')
print(df.sort_index(axis=1))
print('df.sort_index(axis=1,ascending=False)::::::::::::::::::')
print(df.sort_index(axis=1,ascending=False))  #倒序
df=pd.DataFrame({'b':[4,2,3,61],'a':[12,22,22,1]})
print(df)
print(df.sort_values(by='b'))
print(df.sort_values(by=['a','b']))

#计算统计
print(df.count)        #非NA值的数量
print('df.describe()::::::::::::')
print(df.describe())   #列计算汇总统计
print('df.min::::::::')
print(df.min)          #计算最小值
print(df.max)           #计算最大值
print(df)
print(df.idxmin())        #最小值索引值   print(df.idxmin(axis=1))
print(df.idxmax())        #最大值索引值   print(df.idxmax(axis=1))
print(df.quantile())      #样本的分位数
print(df.sum())             #总和
print(df.mean())            #平均数
print(df.median())            #算数中位数
print(df.mad())             #根据平均值计算平均绝对离差
print(df.var())             #样本的方差
print(df.std())             #样本标准差
print(df.cumsum())          #样本值的累计和
print(df.cummax())          #累计最大值
print(df.cummin())          #累计最小值
print(df.cumprod())         #样本值的累计积
print(df.diff())            #计算一阶差分
print(df.pct_change())      #计算百分数变化