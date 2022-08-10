from posixpath import abspath
import re
from unittest import result
from urllib import response
import urllib.request
import interface_link9
import class_link9
import json
import sys
import os 
absPath = os.path.abspath(os.path.join(os.getcwd(),".."))
sys.path.append(abspath)
sys.path.append(os.getcwd())

from utils import detectFullParams
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
       #print(interface_link9.all_interface_link[1])
       for m1 in range(len(interface_link9.all_interface_link)):
              url = interface_link9.all_interface_link[m1]
              with open(url,'r',encoding='utf-8') as f:
                     try:
                            interface_html = f.read()
                     except:
                            continue
              #print(interface_html)
              
              #print("{")
              package_content = re.findall('<div class="header">(.*?)<div class="contentContainer">',interface_html,re.S)
              p = re.compile(r'<div class="subTitle"><span class="packageLabelInType">.*?tml">(.*?)</a></div>')
              m2 = p.findall(str(package_content))
              if m2 == []:continue
              m2 = m2[-1]
              p = re.compile(r'<h2 title="Interface (.*)" class="title">', re.MULTILINE)
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


#DONE:提取Method的Parameter
              #从Method Detail提取 HTML符号是ul li l里的dd 名字在h4
              #------------------Method Detail:---------------------------------
              content_methon = re.findall('<h3>Method Detail</h3>(.*?)<!-- ========= END OF CLASS DATA ========= -->',interface_html,re.S)
              content = str(content_methon)
              menthon_list1 = list()
              method_DictList = []
              p = re.compile('<li class="blockList">(.*?)</li>',re.S)
              for j in p.findall(content):
                     menthon_list1.append(j)
              dict_method = dict()

              for x1 in range(len(menthon_list1)):
                     #先提取类型，然后按顺序赋予挖掘出来的

                     #print("Methon:")
                     methon = re.findall(r'<h4>(.*?)</h4>',menthon_list1[x1])
                     if methon[0] == 'fields':
                         print("stop")
                     Parameter = detectFullParams(str(menthon_list1[x1]),methon)
                     '''if methon[0] == "createContext": 
                            print("stop")
                     print(menthon_list1[x1])
                     print("\n")
                     Parameter = detectParam(str(menthon_list1[0]))
                     print(Parameter)'''
                                          #若<code>包裹了<a href?>则这一块属于Throw
                     #只有数字就是Since
                     #print(Parameter)
                     Parameter_Type = []
                     #TODO:parameter参数类型提取的部分里面有的并不是超链接，比如Int
                     #甚至还有javax.script.Bindings.SimpleBindings.putAll(Map<? extends String,? extends Object> toMerge)这样的 这种线忽略掉
                     #两种情况举例：java.aws.ScrollPaneAdjustable的	removeAdjustmentListener 和 setMinimum
                     #"['void&nbsp;setMinimum(int&nbsp;min)']"
                     #2022-8-1 要不转换思路，从另一个位置进行读取吧 从<td class="colLast">这里提取
                     '''for p in Parameter:
                            #match_Sequence = rf'title=".*?">(.*?)</a>&nbsp;{p}\)</code>'
                            p_type_mid = re.findall(r'<pre>(.*?)</pre>',menthon_list1[x1])
                            p_type = str(p_type_mid).split(f"</a>&nbsp;{p}")[0].split(">")[-1]
                            if p_type[0].isalpha():
                                   Parameter_Type.append(p_type)
                            else:
                                   print(p_type) '''
                     throw_content = re.findall(r'<dt><span class="throwsLabel">(.*?)</dl>',menthon_list1[x1])
                     #throw = re.findall(r'<dd><code><a href=".+">(.*?)</a></code>',str(throw_content))
                     if re.search(r'<dd><code><a href=".+">(.*?)</a></code>',str(throw_content)):
                            throwtext = re.search(r'<dd><code><a href=".+title="class in (.*?)">(.*?)</a></code>',str(throw_content))
                            throw = throwtext.group(1)+'.'+throwtext.group(2)
                     else:
                            throw = []
                     
                     
                     #dict_method[str(methon[0])]={"Parameter":Parameter,"Throw":throw}
                     method_DictList.append({str(methon[0]):{"Parameter":Parameter,"Throw":throw}})
                     
              try:
                     result_dict[json_num] = merge(m2,m3,imple_interface3,imple_interface31,imple_class3,method_DictList)
                     json_num+=1
              except:
                     continue
       with open("interface_result9.json","w") as f:
              json.dump(result_dict,f)
if __name__ == "__main__":
       main()
   

    
