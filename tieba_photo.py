
# coding:utf-8

import urllib.request

import re

def get_html(url):

    page = urllib.request.urlopen(url)

    html = page.read().decode('utf-8')

    return html

reg = r'src="(.+?\.jpg)" width'#正则表达式
reg_img = re.compile(reg)#编译一下，运行更快
imglist = reg_img.findall(get_html('http://tieba.baidu.com/p/1753935195'))#进行匹配
for img in imglist:
    print (img)
