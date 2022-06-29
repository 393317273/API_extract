import re
from urllib import response
import urllib.request
import interface_link
import class_link


def main():
       for m1 in range(len(class_link.all_class_link)):
              url = class_link.all_class_link[m1]
              response = urllib.request.urlopen(url)
              class_html = response.read()
              class_html = class_html.decode("utf-8")
              #print(interface_html)

              
              print("{")
              package_content = re.findall('<div class="header">(.*?)<div class="contentContainer">',class_html,re.S)
              p = re.compile(r'<div class="subTitle">(.*?)</div>')
              for m2 in p.findall(str(package_content)): 
                     print("Package:")
                     print(m2)


              p = re.compile(r'<h2 title="Interface(.*)" class="title">', re.MULTILINE)
              for m3 in p.findall(class_html):
                     print("Interface:")
                     print(m3)

              
              #------------------Superinterfaces:---------------------------------
              content_interface = re.findall('<dt>All Superinterfaces:</dt>(.*?)</dl>',class_html,re.S)
              imple_interface1 = list()
              p = re.compile(r'title="interface in(.*?)">')
              for j in p.findall(str(content_interface)):
                     imple_interface1.append(j)
                     #print(imple_interface1[1])
              content_interface = re.findall('<dt>All Superinterfaces:</dt>(.*?)</dl>',class_html,re.S)
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
              content_interface = re.findall('<dt>All Known Subinterfaces:</dt>(.*?)</dl>',class_html,re.S)
              imple_interface1 = list()
              p = re.compile(r'title="interface in(.*?)">')
              for j in p.findall(str(content_interface)):
                     imple_interface1.append(j)
                     #print(imple_interface1[1])
              content_interface = re.findall('<dt>All Known Subinterfaces:</dt>(.*?)</dl>',class_html,re.S)
              imple_interface2 = list()
              p = re.compile(r'">(.+?)</a>')
              for j in p.findall(str(content_interface)):  
                     imple_interface2.append(j)
                     #print(imple_interface2[1])
              print("Subinterfaces:")
              imple_interface3 = list()
              for l in range(len(imple_interface1)):
                     k = imple_interface1[l] + '.' +imple_interface2[l]
                     imple_interface3.append(k)
              print(imple_interface3)

              #------------------Implementing Classes:---------------------------------
              content_class = re.findall('<dt>All Known Implementing Classes:</dt>(.*?)</dl>',class_html,re.S)
              imple_class1 = list()
              p = re.compile(r'title="class in(.*?)">')
              for j in p.findall(str(content_class)):
                     imple_class1.append(j)
                     #print(imple_interface1[1])
              content_class = re.findall('<dt>All Known Implementing Classes:</dt>(.*?)</dl>',class_html,re.S)
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
              print(imple_class3)


              #------------------Method Detail:---------------------------------
              content_methon = re.findall('<h3>Method Detail</h3>(.*?)<!-- ========= END OF CLASS DATA ========= -->',class_html,re.S)
              content = str(content_methon)
              menthon_list1 = list()
              p = re.compile('<li class="blockList">(.*?)</li>',re.S)
              for j in p.findall(content):
                     menthon_list1.append(j)
              for x1 in range(len(menthon_list1)):
                     print("Methon:")
                     methon = re.findall(r'<h4>(.*?)</h4>',menthon_list1[x1])
                     print(methon)

                     print("Parameter:")
                     Parameter_content1 = re.findall(r'<pre>.*\((.*?)\)',menthon_list1[x1])
                     #print(Parameter_content1)
                     Parameter = re.findall(r'title="class in(.*?)">(.*?)</a>&nbsp;(.*?),''',str(Parameter_content1))
                     print(Parameter)
                     

                     print("Throw:")
                     throw_content = re.findall(r'<dt><span class="throwsLabel">(.*?)</dl>',menthon_list1[x1])
                     throw = re.findall(r'<dd><code><a href=".+">(.*?)</a></code>',str(throw_content))
                     print(throw)
                     '''throw_content = re.findall(r'<dt><span class="throwsLabel">(.*?)</dl>',menthon_list1[x1])
                     p = re.compile('\w.*</a></code>',re.S)
                     for j in p.findall(content):
                     print(j)'''
              
              print("}")
              print("\n")
              

       
if __name__ == "__main__":
       main()
       
