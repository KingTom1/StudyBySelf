import numpy as np

a = 'abcdef'
b = np.fromstring(a,dtype=np.int8)
print(b)

print(np.sin(b)) # 正弦

def func(i,j):
    return i*j
a = np.fromfunction(func,(5,6))  # (5,6)代表5行6列  i和j代表每个数在位置的行号和列号
print(a)
