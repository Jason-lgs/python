
# coding:utf-8

import urllib.request

import re

 

def get_html(url):

    page = urllib.request.urlopen(url)

    html = page.read().decode('utf-8')

    return html

 

reg = r'src="(.+?\.jpg)" width'

reg_img = re.compile(reg)

imglist = reg_img.findall(get_html('http://tieba.baidu.com/p/1753935195'))

x = 0

for img in imglist:

    urllib.request.urlretrieve(img, '%s.jpg' %x)

    x += 1
