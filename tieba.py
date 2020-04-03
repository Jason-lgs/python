import urllib.request
page = urllib.request.urlopen('http://tieba.baidu.com/p/1753935195')
htmlcode = page.read()
htmlcode =  htmlcode.decode('utf-8')
print (htmlcode)
