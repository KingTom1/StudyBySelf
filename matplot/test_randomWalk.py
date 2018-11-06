# coding=utf-8
import matplotlib.pyplot as plt
from randomwalk import randomwalk

# 实例化类
rw =  randomwalk()

rw.fill_walk()

plt.scatter(rw.x_values,rw.y_values,s=15)

plt.show()
