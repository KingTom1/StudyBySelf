#########################Dict 练习####################################
# Dictionary 词典类型， 即是Hash数组。
# 定义方式：arr = {元素k:v}
dict1={} #建立一个空字典
print(type(dict1))
dict1['A1']=3   #新增键值对 第一种方法
dict1.setdefault('B1',2)  #新增键值对 第二种方法
dict1.setdefault('C1','123212')
print(dict1.get('A2','00000'))
del dict1['A1']  #删除指定键值对
dict1['A1']=6
print(dict1.keys())
print(dict1.values())
dict2={}
dict2.update(dict1)   #把dict1的元素加入到dict2中去，键字重复时会覆盖dict2中的键值
print(dict2)
dict1.clear()  #清除Dict
dict3={'a':1,'b':2}
print(dict3)