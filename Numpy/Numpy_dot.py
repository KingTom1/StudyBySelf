import numpy as np
a1 = np.array([[1,2,3],[4,5,6]])
a2 = np.array([[1,2],[3,4],[5,6]])

# 点乘计算 dot()
print(a1.shape[1]==a2.shape[0])
print(a1.dot(a2))

# 矩阵的转置
print(np.array([[1,2,3],[4,5,6]]).transpose())

# 结果为  [[1,4],[2,5],[3,6]]

# 矩阵的转置 方法二
print(np.array([[1,2,3],[4,5,6]]).T)