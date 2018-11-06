import numpy as np
from numpy.random import randn
# Numpy最重要的一个特点就是其N维数组对象【即ndarray】，该对象是一个快速而灵活的大数据集容器。
# 创建ndarray
data = randn(2, 3)
print(data)
print(data.dtype)
print(data.shape)
data2=np.arange(9).reshape((3,3))
arr2=np.array(data2)
print(arr2)
print(arr2.ndim)
# 数组与标量直接的计算
print(arr2*arr2)
print(arr2/2)
# 基本的索引和切片
print(arr2[2])
print(arr2[1:])
# 当切片的值被更新后，会直接反应到源数组上
arr_s=arr2[2]
arr_s[1]=5
print(arr2)
print(arr2[0,2])
# 三维
arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr3=np.arange(27).reshape((3,3,3))
print(+arr3)
print(arr3[1])
# arr3[0]=[[ 117 , 118  ,119], [110 ,112 ,113]]
print(arr3[0])
print(arr3[0:1,0:])
print(arr3[0,1,2])
print(arr3[0,1:2,0])
#转置 轴对换
print(arr3.T)
print('计算矩阵內积')
print(arr2)
print(np.dot(arr2.T,arr2))
#一元函数
print(np.abs(arr2)) #计算各元素的绝对值
print(np.exp(arr2)) #计算各元素指数
print(np.sqrt(arr2)) #计算各元素平方根
print(np.square(arr2)) #计算各元素平方
print(np.sign(arr2)) #计算各元素的正负号 ：1正数 0零 -1负数

#二元函数
print(np.add(arr2,arr2))     #数组相加
print(np.subtract(arr2,arr2))  #数组相减
print(np.multiply(arr2,arr2))   #数组相乘
print(np.divide(arr2,arr2))     #数组相除



