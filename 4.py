#coding=utf-8
#试题3-计算三角形面积
from math import *
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
p=(a+b+c)*0.5
A=sqrt(p*(p-a)*(p-b)*(p-c))
print(A)