# coding=utf-8
# 导入模块
import matplotlib.pyplot as plt

# 数据
squares = [1,4,9,16,25]

# 绘制图形: 曲线图
# plt.plot(squares)
# 绘制图形
# plt.show()

# 绘制    散点图
# x 轴
x = list(range(4))
# y 轴
y = [a**2 for a in x]
plt.scatter(x,y,c='red',marker='>')

# 渐变色 数据大时  呈现渐变曲线效果   plt.scatter(x,y,c=y,cmap=plt.cm.Blues)
plt.show()