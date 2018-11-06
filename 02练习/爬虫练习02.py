# coding =utf-8
import re
import urllib.request

def page(pg):
    url='https://www.pengfu.com/index_%s.html'%pg
    html=urllib.request.urlopen(url).read()
    print(html)
sss=re.search()
page(pg=1)
