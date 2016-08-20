#coding=utf-8
#
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'https://docs.python.org/3/'
sohu=urlopen(url)
soup=BeautifulSoup(sohu,'html.parser')
print(soup.get_text())
#href=soup.find_all('a')
#for link in href:
#	if 'href' in link.attrs:
#		print(link.attrs['href'])
f = open('/users/admin/desktop/1.txt','w')
f.write(str(soup.get_text())+'\n')
f.close()