#coding=utf-8
#自己编写的函数
#1.一元二次方程组
import math

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

delta=b*b-4*a*c
    
if delta<0:
	print('此题无解')
    	
elif delta>0:
	x1= (-b+math.sqrt(delta))/(2*a)
	x2= (-b-math.sqrt(delta))/(2*a)
	print(x1,x2)

else:
    print((-b)/(2*a));



