#!/usr/bin/env python
import re
import urllib

def gethtml(orurl):
    page = urllib.urlopen(orurl)
    html = page.read()
    return html

def getimagurl(html):
    re_html = r'"(http://\S*?\.jpg)"'
    re_html_o = re.compile(re_html)
    imagurl = re_html_o.findall(html)
    return imagurl

def downloadimag(imagurl):
    x = 1
    for imag in imagurl:
        urllib.urlretrieve(imag,'%s.jpg'%x)
        x += 1

html = gethtml("http://www.nuomi.com/?cid=002540")
imagurl = getimagurl(html)
downloadimag(imagurl)
