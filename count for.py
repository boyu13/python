def xiao(values):
	xiao = None
	for i in values:
		if xiao is None or i < xiao:
			xiao = i
	return xiao

x=[1,23,58,99]
print(xiao(x))
