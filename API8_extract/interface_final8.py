from posixpath import abspath
import re
from unittest import result
from urllib import response
import urllib.request
import interface_link8
import class_link8
import json
import sys
import os 
absPath = os.path.abspath(os.path.join(os.getcwd(),".."))
sys.path.append(abspath)
sys.path.append(os.getcwd())
from utils import detectFullParams
#DONE: 改进正则表达式，去掉interface,method,subinterface可能出现的空格
# interface是str，method给到是元组，subinterface一般是list
#TODO:会不会把deprecated也录进去？
#TODO:同名方法无法检测到，会直接忽略掉第二个
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
       for m1 in range(len(interface_link8.all_interface_link)):
              url = interface_link8.all_interface_link[m1]
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
              m2 = m2[-1]
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

              #DONE:提取Method的Parameter
              #从Method Detail提取 HTML符号是ul li l里的dd 名字在h4
              #DONE: 提取interface的参数类型 在哪里啊？
              #method detail里，有超链接
              #<td class="colLast"><code><span class="memberNameLink"><a href="../../java/applet/AppletContext.html#getImage-java.net.URL-">getImage</a></span>(<a href="../../java/net/URL.html" title="class in java.net">URL</a>&nbsp;url)</code>
              #td code span a href的最后一个部分
              #------------------Method Detail:---------------------------------
              content_methon = re.findall('<h3>Method Detail</h3>(.*?)<!-- ========= END OF CLASS DATA ========= -->',interface_html,re.S)
              content = str(content_methon)
              menthon_list1 = list()
              p = re.compile('<li class="blockList">(.*?)</li>',re.S)
              for j in p.findall(content):
                     menthon_list1.append(j)
              dict_method = dict()
              Parameter_content1 = []
              for x1 in range(len(menthon_list1)):
                     #先提取类型，然后按顺序赋予挖掘出来的
                     #TODO:有的方法名重复，仅形参不同，想个办法
                     #print("Methon:")
                     methon = re.findall(r'<h4>(.*?)</h4>',menthon_list1[x1])
                     Parameter = detectFullParams(str(menthon_list1[x1]),methon)
                     #print(Parameter)
                     #print("Parameter:")
                     #2022-8-1 基于正则表达式的参数识别宣布弃用 完全无法使用,使用bs4

                     '''                  
                     del Parameter_content1
                     Parameter_content1 = re.findall(r'<dt><span class="paramLabel">(.*?)<span class="returnLabel">',menthon_list1[x1])
                     if len(Parameter_content1) == 0:
                     #没有return标
                            Parameter_content1 = re.findall(r'<dt><span class="paramLabel">(.*?)</dl>\\n',menthon_list1[x1])
                     #print(Parameter_content1)  
                     #Parameter = re.findall(r'title="class in(.*?)">(.*?)</a>&nbsp;(.*?),',str(Parameter_content1))
                     #Parameter_Mid = re.findall(r'<dd>(.*?)</dd>',str(Parameter_content1))
                     #Parameter_Candidate = []
                     Parameter = []
                     #Parameter_Throw = []
                     for Candidate in re.findall(r'<code>(.*?)</code> -??',str(Parameter_content1)):
                            if not Candidate.isalpha():
                                   continue
                            elif re.findall(r'null',Candidate)!=[]: continue #null failsafe，按规则应该不会识别到
                            Parameter.append(Candidate)
                     #Parameter = re.findall(r'<code>(.*?)</code>',str(Parameter_Candidate))
                     '''
                     #若<code>包裹了<a href?>则这一块属于Throw
                     #只有数字就是Since
                     #print(Parameter)
                     Parameter_Type = []
                     #TODO:parameter参数类型提取的部分里面有的并不是超链接，比如Int
                     #甚至还有javax.script.Bindings.SimpleBindings.putAll(Map<? extends String,? extends Object> toMerge)这样的 这种线忽略掉
                     #两种情况举例：java.aws.ScrollPaneAdjustable的	removeAdjustmentListener 和 setMinimum
                     #"['void&nbsp;setMinimum(int&nbsp;min)']"
                     #2022-8-1 要不转换思路，从另一个位置进行读取吧 从<td class="colLast">这里提取
                     '''
                     for p in Parameter:
                            #match_Sequence = rf'title=".*?">(.*?)</a>&nbsp;{p}\)</code>'
                            p_type_mid = re.findall(r'<pre>(.*?)</pre>',menthon_list1[x1])
                            p_type = str(p_type_mid).split(f"</a>&nbsp;{p}")[0].split(">")[-1]
                            if p_type[0].isalpha():
                                   Parameter_Type.append(p_type)
                            else:
                                   print(p_type)
                     '''
                     #print("Throw:")
                     throw_content = re.findall(r'<dt><span class="throwsLabel">(.*?)</dl>',menthon_list1[x1])
                     #throw = re.findall(r'<dd><code><a href=".+">(.*?)</a></code>',str(throw_content))
                     if re.search(r'<dd><code><a href=".+">(.*?)</a></code>',str(throw_content)):
                            throwtext = re.search(r'<dd><code><a href=".+title="class in (.*?)">(.*?)</a></code>',str(throw_content))
                            throw = throwtext.group(1)+'.'+throwtext.group(2)
                     else:
                            throw = []
                     
                     #TODO: 有的包会存在同名方法（譬如java.util.concurrent.LinkedTransferQueue.try），这样处理的话会被覆盖！
                     dict_method[str(methon[0])]={"Parameter":Parameter,"Throw":throw}
              try:
                     result_dict[json_num] = merge(m2,m3,imple_interface3,imple_interface31,imple_class3,dict_method)
                     json_num+=1
              except:
                     continue
       with open("interface_result8.json","w") as f:
              json.dump(result_dict,f)
if __name__ == "__main__":
       main()
   

    
