# coding=utf-8
arr=[] #创建一个空列表
total=0
values = input('请输入:')
while values != 'Done':
	arr.append(float(values))
	values = input('请输入:')
	
print('总和='+str(sum(arr)))
print('总人数='+str(len(arr)))
print('平均值='+str(sum(arr)/len(arr)))
