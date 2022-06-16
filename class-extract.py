from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re
 
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
	#	self.title_flag = False
	#	self.time_flag = False
 
	#处理开始标签，这里的attrs获取到的是属性列表，属性以元组方式表示
	#获取class,选取需要的标签
	def handle_starttag(self, tag, attrs):
      #  if tag == 'span' and _attr(attrs, 'class') == 'interfaceName':
		#	self.location_flag = True
		if tag == 'span' and _attr(attrs, 'class') == 'interfaceName':
			self.location_flag = True
    # if tag == 'a' and re.match(r'^/events/python-events/(\w{3})/$', _attr(attrs, 'href')):
	#		self.title_flag = True
	#	elif tag == 'span' and _attr(attrs, 'class') == 'event-location':
	#		self.location_flag = True
	#	elif tag == 'time':
	#		self.time_flag = True
		else:
			self.location_flag = False
		#	self.title_flag = False
		#	self.time_flag = False
 
	#处理结束标签，比如</div>
	def handle_endtag(self, tag):
		pass
 
	#处理自己结束的标签，比如<img/>
	def handle_startendtag(self, tag, attrs):
		pass
 
	#处理数据，标签之间的文本,可以加上判断条件，获取所有p标签的文本
	def handle_data(self, data):
		if self.location_flag == True:
			print('class:', data)
			self.location_flag = False		#这一步赋值给flag是避免在后面判断时，相应flag始终为True
	"""	elif self.location_flag == True:
			print('event-location:', data)
			self.location_flag = False
		elif self.time_flag == True:
			print('time:', data)
			self.time_flag = False """
 
	#处理注释，<!-- -->之间的文本
	def handle_comment(self, data):
		pass
 
	def handle_entityref(self, name):
		pass
 
	def handle_charref(self, name):
		pass
 
if __name__ == "__main__":
	url = "file:///C:/docs/api/allclasses-frame.html"
	with request.urlopen(url) as data:		#打开url并获取信息，获取到的数据为bytes类型
		data = data.read()
	parser = MyHTMLParser()
	parser.feed(data.decode('utf-8'))		#进行编码
