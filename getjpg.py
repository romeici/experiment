#coding=utf-8

from urllib.request import urlopen 
from urllib.request import urlretrieve

import re

def getHtml(url):
    page = urlopen(url)
    html = page.read()
    return html

def getImg(html):
    html = html.decode('utf-8')
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print(imglist)
    x = 0
    for imgurl in imglist:
        urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

html = getHtml("http://tieba.baidu.com/p/2460150866")

print(getImg(html))
