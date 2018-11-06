import pandas as pd
import numpy as np
import re
import urllib.request
print ('123123')
print('100 + 200 =', 100 + 200)
#name = input('please enter your name: ')
#print('hello,', name)
#s = pd.Series([1,3,5,np.nan,6,8])
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,5), index=dates, columns=list('ABCDE'))
print (df)
#print (df.T)
#print (df.head(3))
#print (df.tail(3))
#print (df.describe())
#print (df.sort_index(axis=1, ascending=False))
#print (df['A'])
#print (df[0:3])
#print (df.loc['20130102':'20130104',['A','B']])
#print (df.loc['20130102','A'])
#print (df[df.A > 0])

df2 = df.copy()
df2['ttt'] = ['one', 'one','two','three','four',12]
print (df2[df2<0])
dd='20140101'
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range(dd, periods=6))
print(s1)

df['F'] = s1
print (df[df >0])
print (df.dropna(how='any'))

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        print('END2')
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    print(n)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['asd']=312
if 'Thomas' in d:
    a=1
else :
    d['Thomas']=30
print(d['Thomas'])

df3 = pd.Series({'1':100,'2':100,'3':200},index= ['1','3','2'])
print (df3)

dd= pd.Series(np.arange(5),index=np.arange(11,1,-2))
print (dd)
def diaoyong(a,b):
    c=a+b;
    return c