'''from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re
import urllib.request
 
#这个函数用来获取属性
def _attr(attrlist, attrname):
	for attr in attrlist:
		if attr[0] == attrname:
			return attr[1]
	return None
 
class MyHTMLParser(HTMLParser):
	#增加实例属性作为标志
	def __init__(self):
		HTMLParser.__init__(self)
		self.location_flag = False
	
 
	#处理开始标签，这里的attrs获取到的是属性列表，属性以元组方式表示
	#获取class,选取需要的标签
	def handle_starttag(self, tag, attrs):
     
		#if tag == 'span' and _attr(attrs, 'class') == 'interfaceName':
		#	self.location_flag = True
		if tag == 'a' and re.match(r'[java/ org/]', _attr(attrs, 'href')):
			self.location_flag = True
  
		else:
			self.location_flag = False
	
 
	#处理结束标签，比如</div>
	def handle_endtag(self, tag):
		pass
 
	#处理自己结束的标签，比如<img/>
	def handle_startendtag(self, tag, attrs):
		pass
 
	#处理数据，标签之间的文本,可以加上判断条件，获取所有p标签的文本
	def handle_data(self, data):
		if self.location_flag == True:
			print('package:', data)
			self.location_flag = False		#这一步赋值给flag是避免在后面判断时，相应flag始终为True
	
 
	#处理注释，<!-- -->之间的文本
	def handle_comment(self, data):
		pass
 
	def handle_entityref(self, name):
		pass
 
	def handle_charref(self, name):
		pass
 
if __name__ == "__main__":
	url = "file:///C:/docs/api/overview-frame.html"
	with request.urlopen(url) as data:		#打开url并获取信息，获取到的数据为bytes类型
		data = data.read()
	parser = MyHTMLParser()
	parser.feed(data.decode('utf-8'))		#进行编码'''

import re
from urllib import response
import urllib.request
'''response = urllib.request.urlopen("file:///C:/docs/api/overview-frame.html")
#response = urllib.request.urlopen("file:///C:/docs/api/java/lang/package-frame.html")
html = response.read()
html = html.decode("utf-8")'''


url = "file:///C:/docs/api/overview-frame.html"
response = urllib.request.urlopen(url)
html = response.read()
html = html.decode("utf-8")
#print(html)

#获取包名
'''p = re.compile(r'target="packageFrame">(.*)</a>', re.MULTILINE)
for one in p.findall(html):
    print(one)'''


base = "file:///C:/docs/api/"

link=list()
p = re.compile(r'<li><a href="(.*)" target="packageFrame">', re.MULTILINE)
for i in p.findall(html):
		link.append(i)
		#print (link)  #把链接存入了link列表中

linkpath = list()
for i in link:
	i = base +i
	linkpath.append(i)
#print(linkpath)
# 'C:/docs/api/java/applet/package-frame.html'


#url = 'file:///C:/docs/api/java/applet/package-frame.html'
url = linkpath[1]
response = urllib.request.urlopen(url)
html = response.read()
html = html.decode("utf-8")
print(html)





#r=requests.get(url_1)


#获取包的链接
'''p = re.compile(r'<li><a href="(.*)" target="packageFrame">', re.MULTILINE)
for one in p.findall(html):
    print(one)'''

	
