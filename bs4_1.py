# coding=utf-8
# URLLIB &　bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen ('http://www.6park.com')
parks = BeautifulSoup(html,"html.parser")
for link in parks.find_all('a'): #寻找所有的a标签
	if 'href' in link.attrs: #href是标签a里的一个属性
		print(link.attrs['href'])
	