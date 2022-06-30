import re
from unittest import result
from urllib import response
import urllib.request
import interface_link
import class_link
import json


def merge(package, interface, super_Interface, imple_Class, sub_Interface, method):
       dict1 = {"Package":package,"Interface":interface,"Superinterface":super_Interface,
                     "Implementing Class":imple_Class,"Subinterface":sub_Interface,"Method":method}
       #result = json.dumps(dict1)
       return dict1

def main():
       json_num = 0
       result_dict = {}
       for m1 in range(len(interface_link.all_interface_link)):
              url = interface_link.all_interface_link[m1]
              with open(url,'r',encoding='utf-8') as f:
                     try:
                            interface_html = f.read()
                     except:
                            continue
              #print(interface_html)
              
              #print("{")
              package_content = re.findall('<div class="header">(.*?)<div class="contentContainer">',interface_html,re.S)
              p = re.compile(r'<div class="subTitle">(.*?)</div>')
              m2 = p.findall(str(package_content))
              if m2 == []:continue
              m2 = m2[0]
              p = re.compile(r'<h2 title="Interface(.*)" class="title">', re.MULTILINE)
              m3 = p.findall(interface_html)
              if m3 == []:continue
              m3 = m3[0]
              #------------------Superinterfaces:---------------------------------
              content_interface = re.findall('<dt>All Superinterfaces:</dt>(.*?)</dl>',interface_html,re.S)
              imple_interface1 = list()
              p = re.compile(r'title="interface in(.*?)">')
              for j in p.findall(str(content_interface)):
                     imple_interface1.append(j)
                     #print(imple_interface1[1])
              content_interface = re.findall('<dt>All Superinterfaces:</dt>(.*?)</dl>',interface_html,re.S)
              imple_interface2 = list()
              p = re.compile(r'">(.+?)</a>')
              for j in p.findall(str(content_interface)):  
                     imple_interface2.append(j)
                     #print(imple_interface2[1])
              #print("Superinterfaces:")
              imple_interface3 = list()
              for l in range(len(imple_interface1)):
                     k = imple_interface1[l] + '.' +imple_interface2[l]
                     imple_interface3.append(k)
              #print(imple_interface3)


              #------------------Subinterfaces:---------------------------------
              content_interface = re.findall('<dt>All Known Subinterfaces:</dt>(.*?)</dl>',interface_html,re.S)
              imple_interface1 = list()
              p = re.compile(r'title="interface in(.*?)">')
              for j in p.findall(str(content_interface)):
                     imple_interface1.append(j)
                     #print(imple_interface1[1])
              content_interface = re.findall('<dt>All Known Subinterfaces:</dt>(.*?)</dl>',interface_html,re.S)
              imple_interface2 = list()
              p = re.compile(r'">(.+?)</a>')
              for j in p.findall(str(content_interface)):  
                     imple_interface2.append(j)
                     #print(imple_interface2[1])
              #print("Subinterfaces:")
              imple_interface31 = list()
              for l in range(len(imple_interface1)):
                     k = imple_interface1[l] + '.' +imple_interface2[l]
                     imple_interface31.append(k)
              #print(imple_interface31)

              #------------------Implementing Classes:---------------------------------
              content_class = re.findall('<dt>All Known Implementing Classes:</dt>(.*?)</dl>',interface_html,re.S)
              imple_class1 = list()
              p = re.compile(r'title="class in(.*?)">')
              for j in p.findall(str(content_class)):
                     imple_class1.append(j)
                     #print(imple_interface1[1])
              content_class = re.findall('<dt>All Known Implementing Classes:</dt>(.*?)</dl>',interface_html,re.S)
              imple_class2 = list()
              p = re.compile(r'">(.+?)</a>')
              for j in p.findall(str(content_class)):  
                     imple_class2.append(j)
                     #print(imple_interface2[1])
              #print("implement classes:")
              imple_class3 = list()
              for l in range(len(imple_class1)):
                     k = imple_class1[l] + '.' +imple_class2[l]
                     imple_class3.append(k)
              #print(imple_class3)


              #------------------Method Detail:---------------------------------
              content_methon = re.findall('<h3>Method Detail</h3>(.*?)<!-- ========= END OF CLASS DATA ========= -->',interface_html,re.S)
              content = str(content_methon)
              menthon_list1 = list()
              p = re.compile('<li class="blockList">(.*?)</li>',re.S)
              for j in p.findall(content):
                     menthon_list1.append(j)
              dict_method = dict()
              for x1 in range(len(menthon_list1)):
                     #print("Methon:")
                     methon = re.findall(r'<h4>(.*?)</h4>',menthon_list1[x1])
                     #print(methon)

                     #print("Parameter:")
                     Parameter_content1 = re.findall(r'<pre>.*\((.*?)\)',menthon_list1[x1])
                     #print(Parameter_content1)
                     Parameter = re.findall(r'title="class in(.*?)">(.*?)</a>&nbsp;(.*?),''',str(Parameter_content1))
                     #print(Parameter)
                     

                     #print("Throw:")
                     throw_content = re.findall(r'<dt><span class="throwsLabel">(.*?)</dl>',menthon_list1[x1])
                     throw = re.findall(r'<dd><code><a href=".+">(.*?)</a></code>',str(throw_content))
                     #print(throw)
                     
                     
                     dict_method[str(methon[0])]={"Parameter":Parameter,"Throw":throw}
                     
              try:
                     result_dict[json_num] = merge(m2,m3,imple_interface3,imple_interface31,imple_class3,dict_method)
                     json_num+=1
              except:
                     continue
       with open("extract_result.json","w") as f:
              json.dump(result_dict,f)
if __name__ == "__main__":
       main()
   

    
