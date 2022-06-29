import re
from urllib import response
import urllib.request


url = "file:///C:/docs/api/overview-frame.html"
response = urllib.request.urlopen(url)
html_first = response.read()
html_first = html_first.decode("utf-8")


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
#print(link)
#'java/applet/package-frame.html'

linkpath = list()
for i in link:
	i = base +i
	linkpath.append(i)
#print(linkpath)
# 'C:/docs/api/java/applet/package-frame.html'
#print(len(linkpath))

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
#'file:///C:/docs/api/java/applet/package-frame.html'


packagelist = list()
p = re.compile(r'target="packageFrame">(.*)</a>', re.MULTILINE)
for i in p.findall(html_first):
        packagelist.append(i)

   
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
        # #'javax/activation/'
#------------------------------------------------------------------------------------------------------------
for n1 in range(len(linkpath)):
    url = linkpath[n1]
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode("utf-8")
    #print("Packages:")
    #print(packagelist[i+1])#输出Package

    #print("Interfaces:")
    p = re.compile(r'<span class="interfaceName">(.*)</span>', re.MULTILINE)
    for n2 in p.findall(html):
          interfacelist = list()
          interfacelist.append(n2)
          for n3 in range(len(interfacelist)):
               print("Packages:")
               print(packagelist[n1+1])
               print("Interfaces:")
               print(interfacelist[n3])#输出Interface
               print("\n")
               #i= m1  j=m2 k=m3 h=m4


#i= m1  j=m2 k=m3 h=m4
for m1 in range(len(linkpath2)):
    url = linkpath2[m1]
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode("utf-8")
    interface_link1 = list()
    content_interface = re.findall('<ul title="Interfaces">(.*?)</ul>',html,re.S)
    p = re.compile(r'<li><a href="(.*?)" title')
    for m2 in p.findall(str(content_interface)):  
            interface_link1.append(m2)
    #print(link1[i])
    interface_link2 = list()
    for m3 in range(len(interface_link1)):
        base2 = base +link1[m1]+interface_link1[m3]
        interface_link2.append(base2)
    print(interface_link2)
    for m4 in range(len(interface_link2)):
        interface_url = interface_link2[m4]
        response = urllib.request.urlopen(interface_url)
        interface_html = response.read()
        interface_html = interface_html.decode("utf-8")
        content = interface_html
        #print(content)

'''#------------------Superinterfaces:---------------------------------
        content_interface = re.findall('<dt>All Known Superinterfaces:</dt>(.*?)</dl>',content,re.S)
        imple_interface1 = list()
        p = re.compile(r'title="interface in(.*?)">')
        for j in p.findall(str(content_interface)):
           imple_interface1.append(j)
           #print(imple_interface1[1])
        content_interface = re.findall('<dt>All Known Superinterfaces:</dt>(.*?)</dl>',content,re.S)
        imple_interface2 = list()
        p = re.compile(r'">(.+?)</a>')
        for j in p.findall(str(content_interface)):  
          imple_interface2.append(j)
           #print(imple_interface2[1])
        print("Superinterfaces:")
        imple_interface3 = list()
        for l in range(len(imple_interface1)):
           k = imple_interface1[l] + '.' +imple_interface2[l]
           imple_interface3.append(k)
        print(imple_interface3)


          #------------------Subinterfaces:---------------------------------
        content_interface = re.findall('<dt>All Known Subinterfaces:</dt>(.*?)</dl>',content,re.S)
        imple_interface4 = list()
        p = re.compile(r'title="interface in(.*?)">')
        for j in p.findall(str(content_interface)):
           imple_interface4.append(j)
           #print(imple_interface1[1])
        content_interface = re.findall('<dt>All Known Subinterfaces:</dt>(.*?)</dl>',content,re.S)
        imple_interface5 = list()
        p = re.compile(r'">(.+?)</a>')
        for j in p.findall(str(content_interface)):  
          imple_interface5.append(j)
           #print(imple_interface2[1])
        print("Subinterfaces:")
        imple_interface6 = list()
        for l in range(len(imple_interface3)):
           k = imple_interface3[l] + '.' +imple_interface4[l]
           imple_interface6.append(k)
        print(imple_interface6)

          #------------------Implementing Classes:---------------------------------
        content_class = re.findall('<dt>All Known Implementing Classes:</dt>(.*?)</dl>',content,re.S)
        imple_class1 = list()
        p = re.compile(r'title="interface in(.*?)">')
        for j in p.findall(str(content_class)):
           imple_class1.append(j)
           #print(imple_interface1[1])
        content_class = re.findall('<dt>All Known Implementing Classes:</dt>(.*?)</dl>',content,re.S)
        imple_class2 = list()
        p = re.compile(r'">(.+?)</a>')
        for j in p.findall(str(content_class)):  
          imple_class2.append(j)
           #print(imple_interface2[1])
        print("implement classes:")
        imple_class3 = list()
        for l in range(len(imple_class1)):
           k = imple_class1[l] + '.' +imple_class2[l]
           imple_class3.append(k)
        print(imple_class3)'''






'''for m1 in range(len(linkpath2)):
                    url = linkpath2[m1]
                    response = urllib.request.urlopen(url)
                    html = response.read()
                    html = html.decode("utf-8")
                    interface_link1 = list()
                    content_interface = re.findall('<ul title="Interfaces">(.*?)</ul>',html,re.S)
                    p = re.compile(r'<li><a href="(.*?)" title')
                    for m2 in p.findall(str(content_interface)):  
                          interface_link1.append(m2)
                    #print(link1[i])
                    interface_link2 = list()
                    for m3 in range(len(interface_link1)):
                         base2 = base +link1[m1]+interface_link1[m3]
                         interface_link2.append(base2)
                    #print(interface_link2)
                    for m4 in range(len(interface_link2)):
                         interface_url = interface_link2[m4]
                         response = urllib.request.urlopen(interface_url)
                         interface_html = response.read()
                         interface_html = interface_html.decode("utf-8")
                         content = interface_html
                         #print(content)

        #------------------Superinterfaces:---------------------------------
                         content_interface = re.findall('<dt>All Known Superinterfaces:</dt>(.*?)</dl>',content,re.S)
                         imple_interface1 = list()
                         p = re.compile(r'title="interface in(.*?)">')
                         for j in p.findall(str(content_interface)):
                              imple_interface1.append(j)
                               #print(imple_interface1[1])
                         content_interface = re.findall('<dt>All Known Superinterfaces:</dt>(.*?)</dl>',content,re.S)
                         imple_interface2 = list()
                         p = re.compile(r'">(.+?)</a>')
                         for j in p.findall(str(content_interface)):  
                              imple_interface2.append(j)
                              #print(imple_interface2[1])
                         print("Superinterfaces:")
                         imple_interface3 = list()
                         for l in range(len(imple_interface1)):
                              k = imple_interface1[l] + '.' +imple_interface2[l]
                              imple_interface3.append(k)
                         print(imple_interface3)


          #------------------Subinterfaces:---------------------------------
                         content_interface = re.findall('<dt>All Known Subinterfaces:</dt>(.*?)</dl>',content,re.S)
                         imple_interface4 = list()
                         p = re.compile(r'title="interface in(.*?)">')
                         for j in p.findall(str(content_interface)):
                              imple_interface4.append(j)
                               #print(imple_interface1[1])
                         content_interface = re.findall('<dt>All Known Subinterfaces:</dt>(.*?)</dl>',content,re.S)
                         imple_interface5 = list()
                         p = re.compile(r'">(.+?)</a>')
                         for j in p.findall(str(content_interface)):  
                              imple_interface5.append(j)
                               #print(imple_interface2[1])
                         print("Subinterfaces:")
                         imple_interface6 = list()
                         for l in range(len(imple_interface3)):
                              k = imple_interface3[l] + '.' +imple_interface4[l]
                              imple_interface6.append(k)
                         print(imple_interface6)

          #------------------Implementing Classes:---------------------------------
                         content_class = re.findall('<dt>All Known Implementing Classes:</dt>(.*?)</dl>',content,re.S)
                         imple_class1 = list()
                         p = re.compile(r'title="interface in(.*?)">')
                         for j in p.findall(str(content_class)):
                              imple_class1.append(j)
                              #print(imple_interface1[1])
                         content_class = re.findall('<dt>All Known Implementing Classes:</dt>(.*?)</dl>',content,re.S)
                         imple_class2 = list()
                         p = re.compile(r'">(.+?)</a>')
                         for j in p.findall(str(content_class)):  
                              imple_class2.append(j)
                               #print(imple_interface2[1])
                         print("implement classes:")
                         imple_class3 = list()
                         for l in range(len(imple_class1)):
                              k = imple_class1[l] + '.' +imple_class2[l]
                              imple_class3.append(k)
                         print(imple_class3)'''
               
     
'''#i= m1  j=m2 k=m3 h=m4
for m1 in range(len(linkpath2)):
    url = linkpath2[m1]
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode("utf-8")
    interface_link1 = list()
    content_interface = re.findall('<ul title="Interfaces">(.*?)</ul>',html,re.S)
    p = re.compile(r'<li><a href="(.*?)" title')
    for m2 in p.findall(str(content_interface)):  
            interface_link1.append(m2)
    #print(link1[i])
    interface_link2 = list()
    for m3 in range(len(interface_link1)):
        base2 = base +link1[m1]+interface_link1[m3]
        interface_link2.append(base2)
    #print(interface_link2)
    for m4 in range(len(interface_link2)):
        interface_url = interface_link2[m4]
        response = urllib.request.urlopen(interface_url)
        interface_html = response.read()
        interface_html = interface_html.decode("utf-8")
        content = interface_html
        #print(content)

        #------------------Superinterfaces:---------------------------------
        content_interface = re.findall('<dt>All Known Superinterfaces:</dt>(.*?)</dl>',content,re.S)
        imple_interface1 = list()
        p = re.compile(r'title="interface in(.*?)">')
        for j in p.findall(str(content_interface)):
           imple_interface1.append(j)
           #print(imple_interface1[1])
        content_interface = re.findall('<dt>All Known Superinterfaces:</dt>(.*?)</dl>',content,re.S)
        imple_interface2 = list()
        p = re.compile(r'">(.+?)</a>')
        for j in p.findall(str(content_interface)):  
          imple_interface2.append(j)
           #print(imple_interface2[1])
        print("Superinterfaces:")
        imple_interface3 = list()
        for l in range(len(imple_interface1)):
           k = imple_interface1[l] + '.' +imple_interface2[l]
           imple_interface3.append(k)
        print(imple_interface3)


          #------------------Subinterfaces:---------------------------------
        content_interface = re.findall('<dt>All Known Subinterfaces:</dt>(.*?)</dl>',content,re.S)
        imple_interface4 = list()
        p = re.compile(r'title="interface in(.*?)">')
        for j in p.findall(str(content_interface)):
           imple_interface4.append(j)
           #print(imple_interface1[1])
        content_interface = re.findall('<dt>All Known Subinterfaces:</dt>(.*?)</dl>',content,re.S)
        imple_interface5 = list()
        p = re.compile(r'">(.+?)</a>')
        for j in p.findall(str(content_interface)):  
          imple_interface5.append(j)
           #print(imple_interface2[1])
        print("Subinterfaces:")
        imple_interface6 = list()
        for l in range(len(imple_interface3)):
           k = imple_interface3[l] + '.' +imple_interface4[l]
           imple_interface6.append(k)
        print(imple_interface6)

          #------------------Implementing Classes:---------------------------------
        content_class = re.findall('<dt>All Known Implementing Classes:</dt>(.*?)</dl>',content,re.S)
        imple_class1 = list()
        p = re.compile(r'title="interface in(.*?)">')
        for j in p.findall(str(content_class)):
           imple_class1.append(j)
           #print(imple_interface1[1])
        content_class = re.findall('<dt>All Known Implementing Classes:</dt>(.*?)</dl>',content,re.S)
        imple_class2 = list()
        p = re.compile(r'">(.+?)</a>')
        for j in p.findall(str(content_class)):  
          imple_class2.append(j)
           #print(imple_interface2[1])
        print("implement classes:")
        imple_class3 = list()
        for l in range(len(imple_class1)):
           k = imple_class1[l] + '.' +imple_class2[l]
           imple_class3.append(k)
        print(imple_class3)'''



'''#CLASS
        #Implemented Interfaces
        content_interface = re.findall('<dt>All Implemented Interfaces:</dt>(.*?)</dl>',content,re.S)
        imple_interface1 = list()
        p = re.compile(r'title="interface in(.*?)">')
        for j in p.findall(str(content_interface)):
          imple_interface1.append(j)
        #print(imple_interface1[1])

        content_interface = re.findall('<dt>All Implemented Interfaces:</dt>(.*?)</dl>',content,re.S)
        imple_interface2 = list()
        p = re.compile(r'">(.+?)</a>')
        for j in p.findall(str(content_interface)):  
          imple_interface2.append(j)
        #print(imple_interface2[1])

        imple_interface3 = list()
        for l in range(len(imple_interface1)):
               k = imple_interface1[l] + '.' +imple_interface2[l]
               imple_interface3.append(k)
               print(imple_interface3)'''
     






 
 
