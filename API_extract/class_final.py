import re
from unittest import result
from urllib import response
import urllib.request
import interface_link
import class_link
import json


def merge(extend,Package, Class, Implemented_Interfaces, Subclasses, Enclosing_class, field,method):
       dict1 = {"extend":extend,"Package":Package,"Class":Class,"Implemented_Interfaces":Implemented_Interfaces,
                     "Subclasses":Subclasses,"Enclosing_class":Enclosing_class,"Field":field,"Method":method}
       #result = json.dumps(dict1)
       return dict1



def main():
       json_num = 0
       result_dict = {}
       for m1 in range(len(class_link.all_class_link)):
              url = class_link.all_class_link[m1]
              with open(url,'r',encoding='utf-8') as f:
                     try:
                            class_html = f.read()
                     except:
                            continue


              extend_content = re.findall('<div class="contentContainer">(.*?)<div class="description">',class_html,re.S)
              extend_list = list()
              p = re.compile(r'<li><a href=".*">(.*?)</a></li>')
              for m4 in p.findall(str(extend_content)): 
                     extend_list.append(m4)
              #print(extend_list)


              package_content = re.findall('<div class="header">(.*?)<div class="contentContainer">',class_html,re.S)
              package_list = list()
              p = re.compile(r'<div class="subTitle">(.*?)</div>')
              m2 = p.findall(str(package_content))
              if m2 == []:continue
              m2 = m2[-1]
                     # for m2 in p.findall(str(package_content)):
                     #package_list.append(m2)
                     #print("Package:")
                     #print(m2)
              #print(package_list[-1])
              #print(package_list.pop())

              p = re.compile(r'<h2 title="Class(.*)" class="title">', re.MULTILINE)
              m3 = p.findall(class_html)
              if m3 == []:continue
              m3 = m3[0]
              #for m3 in p.findall(class_html):
                     #print("Class:")
                     #print(m3)

              
              #------------------Implemented Interfaces:---------------------------------
              content_interface = re.findall('<dt>All Implemented Interfaces:</dt>(.*?)</dl>',class_html,re.S)
              imple_interface1 = list()
              p = re.compile(r'title="interface in(.*?)">')
              for j in p.findall(str(content_interface)):
                     imple_interface1.append(j)
                     #print(imple_interface1[1])
              content_interface = re.findall('<dt>All Implemented Interfaces:</dt>(.*?)</dl>',class_html,re.S)
              imple_interface2 = list()
              p = re.compile(r'">(.+?)</a>')
              for j in p.findall(str(content_interface)):  
                     imple_interface2.append(j)
                     #print(imple_interface2[1])
              #print("Implemented Interfaces:")
              imple_interface3 = list()
              for l in range(len(imple_interface1)):
                     k = imple_interface1[l] + '.' +imple_interface2[l]
                     imple_interface3.append(k)
              #print(imple_interface3)


              #------------------Direct Known Subclasses::---------------------------------
              content_interface = re.findall('<dt>Direct Known Subclasses:</dt>(.*?)</dl>',class_html,re.S)
              imple_interface1 = list()
              p = re.compile(r'title="class in(.*?)">')
              for j in p.findall(str(content_interface)):
                     imple_interface1.append(j)
                     #print(imple_interface1[1])
              content_interface = re.findall('<dt>Direct Known Subclasses:</dt>(.*?)</dl>',class_html,re.S)
              imple_interface2 = list()
              p = re.compile(r'">(.+?)</a>')
              for j in p.findall(str(content_interface)):  
                     imple_interface2.append(j)
                     #print(imple_interface2[1])
              #print("Subclasses:")
              imple_interface31 = list()
              for l in range(len(imple_interface1)):
                     k = imple_interface1[l] + '.' +imple_interface2[l]
                     imple_interface31.append(k)
              #print(imple_interface3)

              #------------------Enclosing class:---------------------------------
              content_class = re.findall('<dt>Enclosing class:</dt>(.*?)</dl>',class_html,re.S)
              imple_class1 = list()
              p = re.compile(r'title="class in(.*?)">')
              for j in p.findall(str(content_class)):
                     imple_class1.append(j)
                     #print(imple_interface1[1])
              content_class = re.findall('<dt>Enclosing class:</dt>(.*?)</dl>',class_html,re.S)
              imple_class2 = list()
              p = re.compile(r'">(.+?)</a>')
              for j in p.findall(str(content_class)):  
                     imple_class2.append(j)
                     #print(imple_interface2[1])
              #print("Enclosing class:")
              imple_class32 = list()
              for l in range(len(imple_class1)):
                     k = imple_class1[l] + '.' +imple_class2[l]
                     imple_class32.append(k)
              #print(imple_class3)




              #------------------Field Detail:---------------------------------
              content_filed =re.findall('<h3>Field Summary</h3>(.*?)</table>',class_html,re.S) 
              content1 = str(content_filed)
              field_list1 = list()
              p = re.compile('<td class="colFi(.*?)</tr>',re.S)
              for j in p.findall(content1):
                     field_list1.append(j)
              for x1 in range(len(field_list1)):
                     field_name = re.findall(r'<td class="colLast"><code><span class="memberNameLink"><a href=".*">(.*?)</a></span></code>',field_list1[x1])
              #print(field_name)                 
                     type = re.findall(r'st"><code>(.*?) <a href.*" title="class in(.*?)">(.*?)</a></code></td>',str(field_list1[x1]))
              #print(type)                
              dict_field1 = dict()
              dict_field1 = {"Field":field_name,"Type":type}

              #print(dict_field1)


              #------------------Method Detail:---------------------------------
              content_methon = re.findall('<h3>Method Detail</h3>(.*?)<!-- ========= END OF CLASS DATA ========= -->',class_html,re.S)
              content = str(content_methon)
              menthon_list1 = list()
              p = re.compile('<li class="blockList">(.*?)</li>',re.S)
              for j in p.findall(content):
                     menthon_list1.append(j)
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
                     dict_method1 = {"method":methon,"Parameter":Parameter,"Throw":throw}
              try:
                     result_dict[json_num] = merge(extend_list,m2,m3,imple_interface3,imple_interface31,imple_class32,dict_field1,dict_method1)
                     json_num+=1
              except:
                     continue
       with open("class_result.json","w") as f:
              json.dump(result_dict,f)       
              
              #print("}")
              #print("\n")
              

       
if __name__ == "__main__":
       main()
       
