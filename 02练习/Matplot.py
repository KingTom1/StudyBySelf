import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#coding=utf-8

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = np.cos(x), np.sin(x)
# 绘制
plt.figure(1)
# 自变量 因变量
plt.plot(x, c)
# 自变量 因变量
plt.plot(x, s)
plt.show()
# plt.savefig("one.png")

df=pd.read_excel(r'..\\04数据\年报门诊住院病人来源2015.xlsx')
df=df[0:100]
df=df[['出院日期','年龄','总费用']]
# df=pd.DataFrame()

fig=plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)
ax1.hist(df['总费用'])
ax1.set_title('Total',color='y')
ax2.scatter(df['年龄'],df['总费用'],color='k')
ax3.bar(df['年龄'],df['总费用'],color='g')
ax4.barh(df['出院日期'],df['总费用'],color='r')
plt.show()



