###########################List 学习###################################
# list 普通的链表，初始化后可以通过特定方法动态增加元素。
# 定义方式：arr = [元素]
list = ['physics', 'chemistry', 1997, 2000];
list2 = ['12', 'ttt', 1997, 2000];
list[2] = 2001;   #修改指定元素
del list[1]     #删除指定元素
del list2[0:2]
# Python 表达式	结果	描述
# len([1, 2, 3])	3	长度
# [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
# 3 in [1, 2, 3]	True	元素是否存在于列表中
# for x in [1, 2, 3]: print x,	1 2 3	迭代
list3=list+list2
print(list3)
print(len(list3))
print(list3*2)
print(1997 in list3)
for i in list3:
    print(i)
# 列表操作包含以下函数:
# 1、cmp(list1, list2)：比较两个列表的元素
# 2、len(list)：列表元素个数
# 3、max(list)：返回列表元素最大值
# 4、min(list)：返回列表元素最小值
# 5、list(seq)：将元组转换为列表
print(list2)
print(max(list2))

# 列表操作包含以下方法:
# 1、list.append(obj)：在列表末尾添加新的对象
# 2、list.count(obj)：统计某个元素在列表中出现的次数
# 3、list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4、list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
# 5、list.insert(index, obj)：将对象插入列表
# 6、list.pop(obj=list[-1])：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 7、list.remove(obj)：移除列表中某个值的第一个匹配项
# 8、list.reverse()：反向列表中元素
# 9、list.sort([func])：对原列表进行排序
obj={}
list.append('AAA')
print(list)
