import 练习02
a=int('3122')
print(a)
b= abs(-1230)
print(b)
def fun(a,b) :
	if a>0:
		a=100;
	else:
		a=0;
	print(a+b)
c=fun(2,3)
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
d=f1(1,2,3,4,5,6,7,8)
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))
print (练习02.diaoyong(5, 4))