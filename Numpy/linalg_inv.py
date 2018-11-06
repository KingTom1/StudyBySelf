# coding=utf-8
import numpy as np
import numpy.linalg as lg

# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(lg.inv(a))
# 结果
# [[ -4.50359963e+15   9.00719925e+15  -4.50359963e+15]
#  [  9.00719925e+15  -1.80143985e+16   9.00719925e+15]
#  [ -4.50359963e+15   9.00719925e+15  -4.50359963e+15]]

a = np.eye(3)  # 3阶单位矩阵
print(lg.inv(a))  # 单位矩阵的逆为他本身
# 结果
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
