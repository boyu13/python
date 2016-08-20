#coding = utf-8
from bs4 import BeautifulSoup
from urllib.request import urlopen
url="http://www.cool18.com/bbs4/index.php?app=forum&act=threadview&tid=13877759"
x = urlopen(url)
y = BeautifulSoup(x,'html.parser',from_encoding='gb18030')
#print(y.pre)
#print(y.body.get_text())

f = open('/users/admin/desktop/1.txt','a')
f.write(str(y.pre.get_text())+'\n')
f.close()