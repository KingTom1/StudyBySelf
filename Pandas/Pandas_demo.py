# -*- coding:utf8 -*-
from pandas import Series
import pandas as pd
s = Series([1,4,'ww','tt'])
print(s)
print(s.index)
print(s.values)
print(s[2])
s2 = Series(['zhangyuqi','man',24],index=['name','sex','age'])
s2['name']='lixingyue'
print(s2)
s3 = Series({'python':100,'c++':200,'c#':300})
print(s3.isnull())
arr = {'java':120,'python':300}
s4 = Series(arr)
print(s4)
s5 = Series(arr,index=['c++','java','python','c'])
print(s5)
print(s5.isnull())
s5.index=['语文','数学','enlish','java']
print(s5)
print(s5 * 2)
print(s5[s5*2>120])
