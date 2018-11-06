# math库及其random库
'''圆周率pi  '''
import math
math.pi

'''自然常数e'''
math.e

'''ceil(x) 向上取整'''
a = math.ceil(3.2)
print(a)

'''floor(x) 向下取整'''

'''pow(x,y) 计算x的y次方 等效于 x**y'''
b = pow(3,9)
print(b)
b = 3**9
print(b)

'''log(x) 以e为基的对数'''

'''log10(x) 以10为基的对数'''

'''sqrt(x) 平方根'''
print(math.sqrt(5))

'''exp(x)  e的x次幂'''

'''degrees(x)   将弧度值转换成角度'''

'''radians(x)   将角度值转换为弧度'''
print(math.radians(90))
print(math.radians(180))
print(math.degrees(math.pi))

'''random库包含一些随机函数
1. seed(x)  给随机数一个种子值,默认随机种子是系统时钟
2. random()  生成一个[0, 1.0]之间的随机小数
3. uniform(a,b) 生成一个a到b之间的随机小数
4. randint(a,b) 生成一个a到b之间的随机整数
5. randrange(a,b,c)  随机生成一个从a开始到b以c递增的数
6. choice(<list>)  从列表中随机返回一个元素
7. shuffle(<list>) 将列表中元素随机打乱,无返回值'''
import random as rd
a= rd.choice([1,2,3,4,5,6,7,8,9,0])
print(a)

list = [1,2,3,4,5,6,7,8,9,0]
rd.shuffle(list) # 打乱list顺序,没有返回值
print(list)