import re
from urllib import response
import urllib.request
#import load_html


url = "file:///C:/docs/api/overview-frame.html"
response = urllib.request.urlopen(url)
html_first = response.read()
html_first = html_first.decode("utf-8")
#print(html)

#获取包名
packagelist = list()
p = re.compile(r'target="packageFrame">(.*)</a>', re.MULTILINE)
for i in p.findall(html_first):
    packagelist.append(i)
    #print(packagelist)


base = "file:///C:/docs/api/"

link=list()
p = re.compile(r'<li><a href="(.*)" target="packageFrame">', re.MULTILINE)
for i in p.findall(html_first):
		link.append(i)
		#print (link)  #把链接存入了link列表中

linkpath = list()
for i in link:
	i = base +i
	linkpath.append(i)
#print(linkpath)
# 'C:/docs/api/java/applet/package-frame.html'
#print(len(linkpath))


#url = 'file:///C:/docs/api/java/applet/package-frame.html'



packagelist = list()
p = re.compile(r'target="packageFrame">(.*)</a>', re.MULTILINE)
for i in p.findall(html_first):
        packagelist.append(i)




for i in range(len(linkpath)):
    url = linkpath[i]
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode("utf-8")
    print("Packages:")
    print(packagelist[i+1])#输出Package

    print("Interfaces:")
    p = re.compile(r'<span class="interfaceName">(.*)</span>', re.MULTILINE)
    for j in p.findall(html):
        interfacelist = list()
        interfacelist.append(j)
        print(interfacelist)#输出Interface

    print("Classes:")
    content = re.findall('<ul title="Classes">(.*?)</ul>',html,re.S)
    p = re.compile(r'target="classFrame">(.*?)</a>')
    for j in p.findall(str(content)):
        classlist = list()
        classlist.append(j)
        print(classlist)#输出Class

    print("Enums:")
    content = re.findall('<ul title="Enums">(.*?)</ul>',html,re.S)
    p = re.compile(r'target="classFrame">(.*?)</a>')
    for j in p.findall(str(content)):
        enumlist = list()
        enumlist.append(j)
        print(enumlist)#输出Enum

    print("Exceptions:")
    content = re.findall('<ul title="Exceptions">(.*?)</ul>',html,re.S)
    p = re.compile(r'target="classFrame">(.*?)</a>')
    for j in p.findall(str(content)):
        exceptionlist = list()
        exceptionlist.append(j)
        print(exceptionlist)#输出Exceptions

    print("Errors:")
    content = re.findall('<ul title="Errors">(.*?)</ul>',html,re.S)
    p = re.compile(r'target="classFrame">(.*?)</a>')
    for j in p.findall(str(content)):
        errorlist = list()
        errorlist.append(j)
        print(errorlist)#输出Errors
    
    print("Annotation_Types:")
    content = re.findall('<ul title="Annotation Types">(.*?)</ul>',html,re.S)
    p = re.compile(r'target="classFrame">(.*?)</a>')
    for j in p.findall(str(content)):
        Annotation_Typelist = list()
        Annotation_Typelist.append(j)
        print(Annotation_Typelist)#输出Annotation_Types


    print("\n")
   



    
    
    
   
    


    







