# coding=utf-8
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.max())  # 获取整个矩阵的最大值 结果： 6
print(a.min())  # 结果：1

# 可以指定关键字参数axis来获得行最大（小）值或列最大（小）值
# axis=0 行方向最大（小）值，即获得每列的最大（小）值
# axis=1 列方向最大（小）值，即获得每行的最大（小）值
# 例如

print(a.max(axis=0))
# 结果为 [4 5 6]

print(a.max(axis=1))
# 结果为 [3 6]

# 要想获得最大最小值元素所在的位置，可以通过argmax函数来获得
print(a.argmax(axis=1))
# 结果为 [2 2]
