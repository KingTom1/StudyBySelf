Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> data = DataFrame([{'t':'2018-01-08 14:12:26', 'name':'yang'},{'t':'2017-01-08 14:12:26', 'name':'jian'}, {'t':'2014-01-08 14:12:26', 'name':'yj'}])  
print(data)  
  
dd =data.ix[1, 't']  
print('\n',type(dd))  
  
ee = data.ix[[1], 't']  
print('\n', type(ee))  
  
ff = data.ix[1, ['t']]  
print('\n', type(ff))  
  
gg = data.loc[[1], ['t']]  
print('\n',type(gg))
SyntaxError: multiple statements found while compiling a single statement
>>> data = DataFrame([{'t':'2018-01-08 14:12:26', 'name':'yang'},{'t':'2017-01-08 14:12:26', 'name':'jian'}, {'t':'2014-01-08 14:12:26', 'name':'yj'}])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    data = DataFrame([{'t':'2018-01-08 14:12:26', 'name':'yang'},{'t':'2017-01-08 14:12:26', 'name':'jian'}, {'t':'2014-01-08 14:12:26', 'name':'yj'}])
NameError: name 'DataFrame' is not defined
>>> import DataFrame
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import DataFrame
ModuleNotFoundError: No module named 'DataFrame'
>>> import pandas from DataFrame
SyntaxError: invalid syntax
>>> import DataFrame from pandas
SyntaxError: invalid syntax
>>> import
SyntaxError: invalid syntax
>>> import pandas
>>> data = pandas.DataFrame([{'t':'2018-01-08 14:12:26', 'name':'yang'},{'t':'2017-01-08 14:12:26', 'name':'jian'}, {'t':'2014-01-08 14:12:26', 'name':'yj'}])
>>> print(data)
   name                    t
0  yang  2018-01-08 14:12:26
1  jian  2017-01-08 14:12:26
2    yj  2014-01-08 14:12:26
>>> dd = data.ix[1,'t']
>>> print(dd)
2017-01-08 14:12:26
>>> print(type(dd))
<class 'str'>
>>> ee = data.ix[[1], 't']  
print('\n', type(ee))
SyntaxError: multiple statements found while compiling a single statement
>>> ee = data.ix[[1],'t']
>>> print('\n', type(ee))

 <class 'pandas.core.series.Series'>
>>> print(ee)
1    2017-01-08 14:12:26
Name: t, dtype: object
>>> ff = data.ix[1, ['t']]
>>> print(ff)
t    2017-01-08 14:12:26
Name: 1, dtype: object
>>> print(type(ff))
<class 'pandas.core.series.Series'>
>>> gg = data.loc[[1], ['t']]
>>> print(gg)
                     t
1  2017-01-08 14:12:26
>>> 
