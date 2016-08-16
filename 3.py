#coding=utf-8
#试题3-计算任意数的平方根

from math import sqrt
x=float(input('Please enter a number:'))
if x>=0:
    y=sqrt(x)
    print(y)
else:
	print('傻逼了吧')