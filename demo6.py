import re
from urllib import response
import urllib.request
response = urllib.request.urlopen("file:///C:/docs/api/allclasses-frame.html")
html = response.read()
html = html.decode("utf-8")


p = re.compile(r'target="classFrame">(.*)</a>', re.MULTILINE)
for one in p.findall(html):
    print(one)

print("111")

'''p = re.compile(r'<span class="interfaceName">(.*)</span>', re.MULTILINE)
for one in p.findall(html):
    print(one)'''