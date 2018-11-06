###########################Tuple 练习###################################
# Tuple 固定的数组，一旦定义后，其元素个数是不能再改变的。
# 定义方式：arr = (元素)

# Tuple 没有的方法：
# [1] 不能向 tuple 增加元素，没有 append 、 extend 、insert 等方法。
# [2] 不能从 tuple 删除元素，没有 remove 或 pop 方法。
# [3] 不能在 tuple 中查找元素，没有 index 方法（index是查找而不是索引，索引直接用下标即可，如：t[0]）。
t=('1','2','3')
print(t)

# Tuple 可以转换成 list， 反之亦然。转换方式为：
t = list( t )
print(t)
t = tuple( t )
print(t)
