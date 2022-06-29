import re
from urllib import response
import urllib.request


url = "file:///C:/docs/api/overview-frame.html"
response = urllib.request.urlopen(url)
html_first = response.read()
html_first = html_first.decode("utf-8")

base = "file:///C:/docs/api/"

link=list()
p = re.compile(r'<li><a href="(.*)" target="packageFrame">', re.MULTILINE)
for i in p.findall(html_first):
		link.append(i)
#print(link)
#'java/applet/package-frame.html'

linkpath2 = list()
for i in range(len(link)):
    k = base + link[i]
    linkpath2.append(k)
#print(linkpath2)
#'file:///C:/docs/api/java/applet/package-frame.html'


linkpath1 = list()
for i in link:
	i = base +i
	linkpath1.append(i)
#print(linkpath1)

    #print(link1)
    #'javax/activation/'
for i in range(len(linkpath1)):
        url = linkpath1[i]
        response = urllib.request.urlopen(url)
        html = response.read()
        html = html.decode("utf-8")
        link1=list()
        p = re.compile(r'<li><a href="(.*)package-frame.html" target="packageFrame">', re.MULTILINE)
        for i in p.findall(html_first):
            link1.append(i)
        #print(link1)
	

for i in range(len(linkpath2)):
    url = linkpath2[i]
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode("utf-8")
    interface_link1 = list()
    content_interface = re.findall('<ul title="Classes">(.*?)</ul>',html,re.S)
    p = re.compile(r'<li><a href="(.*?)" title')
    for j in p.findall(str(content_interface)):  
            interface_link1.append(j)
    #print(interface_link1)
    interface_link2 = list()
    for k in range(len(interface_link1)):
        base2 = base +link1[i]+interface_link1[k]
        interface_link2.append(base2)
    #print(interface_link2)
    with open('C:/Users/LGH/Desktop/API_extract.txt', 'a+') as f:
            print(interface_link2, file=f)
    
'''for h in range(len(interface_link2)):
        interface_url = interface_link2[h]
        response = urllib.request.urlopen(interface_url)
        interface_html = response.read()
        interface_html = interface_html.decode("utf-8")
        content = interface_html
    with open('C:/Users/LGH/Desktop/API_extract.txt', 'a+') as f:
        print(content, file=f)
        #print(content)'''
