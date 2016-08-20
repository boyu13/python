# coding=utf-8
# URLLIB
from urllib.request import urlopen
html = urlopen ('http://www.6park.com')
print(html.read())