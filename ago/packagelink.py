import re
from urllib import response
import urllib.request

url1 = "file:///C:/docs/api/java/lang/package-frame.html"
response = urllib.request.urlopen(url1)
html = response.read()
html = html.decode("utf-8")
#print(html)

'''print("Interfaces---------------------")
p = re.compile(r'<span class="interfaceName">(.*)</span>', re.MULTILINE)
for one in p.findall(html):
    print(one)'''


print("Classes------------------------")
b = re.findall('<ul title="Enums">(.*?)</ul>',html,re.S)
print(b)

'''p = re.compile(r'target="classFrame">(.*)</a>', re.MULTILINE)
for one in p.findall(b):
    print(one)'''

'''a = re.findall(r'target="classFrame">(.*)</a>', b,re.S)
print(a)'''