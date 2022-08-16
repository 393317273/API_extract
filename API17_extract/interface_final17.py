from posixpath import abspath
import re
from unittest import result
from urllib import response
import urllib.request
import interface_link17
import class_link17
import json
import sys
import os 
absPath = os.path.abspath(os.path.join(os.getcwd(),".."))
sys.path.append(abspath)
sys.path.append(os.getcwd())

from utils import detectFullParams, detectFullParams2
#TODO: 改进正则表达式，去掉interface,method,subinterface可能出现的空格
# interface是str，method给到是元组，subinterface一般是list
def removeSpace(inputStrList):
       inputIsStr = False
       if len(inputStrList)==0: return
       if str(type(inputStrList))=="<class 'str'>":
              inputStrList = [inputStrList]
              inputIsStr = True
       if str(type(inputStrList[0])) == "<class 'tuple'>":
              inputStrList = inputStrList[0]
       resultStr = []
       for inputStr in inputStrList:
              if inputStr[0]==" ":
                     resultStr.append(inputStr[1:])
              else:
                     resultStr.append(inputStr)
       if inputIsStr:
              return resultStr[0]
       return resultStr
def merge(package, interface, super_Interface, imple_Class, sub_Interface, method):
       dict1 = {"Package":package,"Interface":removeSpace(interface),"Superinterface":removeSpace(super_Interface),
                     "Implementing Class":removeSpace(imple_Class),"Subinterface":removeSpace(sub_Interface),"Method":method}
       #result = json.dumps(dict1)
       return dict1

def main():
       json_num = 0
       result_dict = {}
       for m1 in range(len(interface_link17.all_interface_link)):
              url = interface_link17.all_interface_link[m1]
              with open(url,'r',encoding='utf-8') as f:
                     try:
                            interface_html = f.read()
                     except:
                            continue
              #print(interface_html)
              
              #print("{")
              package_content = re.findall('<div class="header">(.*?)<!-- ========== METHOD SUMMARY =========== -->',interface_html,re.S)
              #print(package_content)
              p = re.compile(r'<div class="sub-title"><span class="package-label-in-type">.*?tml">(.*?)</a></div>')
              m2 = p.findall(str(package_content))
              if m2 == []:continue
              m2 = m2[-1]
              #print(m2)
              p = re.compile(r'<h1 title="Interface (.*)" class="title">', re.MULTILINE)
              m3 = p.findall(interface_html)
              if m3 == []:continue
              m3 = m3[0]
              #print(m3)
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
              content_methon = re.findall('<!-- ============ METHOD DETAIL ========== -->(.*?)<!-- ========= END OF CLASS DATA ========= -->',interface_html,re.S)
              content = str(content_methon)
              menthon_list1 = list()
              method_DictList = []
              p = re.compile('<section class="detail"(.*?)</section>',re.S)
              for j in p.findall(content):
                     menthon_list1.append(j)
              dict_method = dict()
              for x1 in range(len(menthon_list1)):
                     #print("Methon:")
                     methon = re.findall(r'<h3>(.*?)</h3>',menthon_list1[x1])
                     '''if methon[0] == 'fields':
                            print("stop")'''
                     Parameter = detectFullParams2(str(menthon_list1[x1]),methon)

                     Parameter_Type = []
                     #Parameter_content1 = re.findall(r'<pre>.*\((.*?)\)',menthon_list1[x1])
                     #print(Parameter_content1)
                     #Parameter = re.findall(r'title="class in(.*?)">(.*?)</a>&nbsp;(.*?)[)]</pre>',str(Parameter_content1))
                     
                     '''Parameter = re.findall(r'<section class="detail" id.*?[(](.*?)[)]">',menthon_list1[x1])'''
                     #print(Parameter)
                     
                    
                     throw_content = re.findall(r'dt>Throws:</dt>(.*?)</dl>',menthon_list1[x1])
                     if re.search(r'<dd><code><a href=".+">(.*?)</a></code>',str(throw_content)):
                            throwtext = re.search(r'<dd><code><a href=".+title="class in (.*?)">(.*?)</a></code>',str(throw_content))
                            throw = throwtext.group(1)+'.'+throwtext.group(2)
                     else:
                            throw = []
                     #throw = re.findall(r'<dd><code><a href=".+">(.*?)</a></code>',str(throw_content))
                     #print(throw)
                     #method_DictList.append({str(methon[0]):{"Parameter":Parameter,"Throw":throw}})
                     if(methon):                 
                            method_DictList.append({str(methon[0]):{"Parameter":Parameter,"Throw":throw}})
                     else:
                            dict_method={} 
                     
              try:
                     result_dict[json_num] = merge(m2,m3,imple_interface3,imple_interface31,imple_class3,method_DictList)
                     json_num+=1
              except:
                     continue
       with open("interface_result17.json","w") as f:
              json.dump(result_dict,f)
if __name__ == "__main__":
       main()
   

    
