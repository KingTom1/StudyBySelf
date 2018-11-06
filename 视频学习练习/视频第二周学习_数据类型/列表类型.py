# 列表(list)是有序的元素集合
# 列表元素可以通过索引访问单个元素
# 列表与元组不同的是: 列表的大小没有限制,可以随时修改
'''
<seq> + <seq>                    连接两个序列
<seq> * <整数类型>              对序列进行整数次重复
<seq> [<整数类型>]              索引序列中的元素
Len(<seq>)                      序列中元素个数
<seq>[<整数类型>:<整数类型>]    取序列的一个子序列
For<var> in <seq>:              对序列进行循环列举
<expr> in <seq>                 expr选项是否在序列中
'''

'''列表的操作'''
vlist = [0,1,2,3,4]
print(vlist*2)  # 扩展列表  输出[0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
print(len(vlist[2:])) # 取从2开始获取[2,3,4]  输出该列表长度 为  3
for i in vlist[:3]:
    print(i)
# 遍历列表 输出
# 0
# 1
# 2
a = 2 in vlist
print(a)
# 判断值是否在列表内 输出true

'''方法:
<list>.append(x)   将元素x增加到列表的最后
<list>.sort()      将列表元素排序
<list>.reverse()   将列表元素反转
<list>.index()     返回第一次出现元素x的索引值
<list>.insert(i,x)  在i处插入新元素x
<list>.pop(i)       取出列表中位置为i的元素,并删除它
<list>.count(x)     返回元素x在列表中的数量
<list>.remove(x)    删除列表中第一个出现的元素x'''

list = "python is an excellent language".split()
print(list)

