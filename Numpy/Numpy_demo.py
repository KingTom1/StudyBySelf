import numpy as np  # 引入numpy库
import matplotlib.pyplot as plt
# 创建一维的narray对象http://10.88.69.104/redmine/projects/learn_train/issues/28402/time_entries
a = np.array([1, 2, 3, 4, 5])
# plt.plot(a)
# plt.show()
# 创建二维的narray对象
a2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
# plt.plot(a2)
# plt.show()
# 创建多维对象以其类推
print(a)
print(a2)

# 通过shape 获取a2对象的各维长度
print(a2.shape)  # 输出tuple元组(2L,5L)
print(a2.shape[0])  # 输出row长度
print(a2.shape[1])  # 输出col长度

# 通过[] 方括号 截取行列
print(a2[2:3])
print(a2[0, 1])    # 结果为具体数值
print(a2[1, 2:4])
print(a2[1, :])

# 通过条件截取,即在[]中传入自身布尔语句,结果依然是数组
print(a2[a2 > 10])

a2[a2 > 10] = a  # 可以赋予一个数据长度对应的数组 或 类型一致的数值
print(a2)   # 输出重新赋值后的值

a3 = np.array([[1, 2, 3], [3, 4, 5],[3, 4, 5]])
a4 = np.array([[5, 6, 7], [7, 8, 9],[3, 4, 5]])
a5 = np.array([[17, 18, 19], [20, 21, 22], [23, 24, 25]])
print(np.hstack([a3, a4]))
#输出 [[1 2 6 5 6] [3 4 5 7 8]]

print(np.vstack((a3,a4,a5)))
