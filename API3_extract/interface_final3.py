import re
from unittest import result
from urllib import response
import urllib.request
import interface_link3
#import class_link
import json
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
       #print(interface_link3.all_interface_link[4000])
       #print(len(interface_link3.all_interface_link))
       for m1 in range(len(interface_link3.all_interface_link)):
              url = interface_link3.all_interface_link[m1]
              with open(url,'r',encoding='utf-8') as f:
                     try:
                            interface_html = f.read()
                     except:
                            continue
              #print(interface_html)
              
              #print("{")
              package_content = re.findall('<H2>(.*?)<DL>',interface_html,re.S)
              p = re.compile(r'<FONT SIZE="-1">\\n(.*?)</FONT>')
              m2 = p.findall(str(package_content))
              if m2 == []:continue
              m2 = m2[-1]
              #print(m2)
              p = re.compile(r'Interface  (.*)</H2>', re.MULTILINE)
              m3 = p.findall(interface_html)
              if m3 == []:continue
              m3 = m3[0]
              #print(m3)
              #------------------Superinterfaces:---------------------------------
              content_class = re.findall('<DT><B>All Superinterfaces:</B> <DD>(.*?)</DL>',interface_html,re.S)
              imple_interface3 = list()
              p = re.compile(r'<A HREF="../../(.*?).html">')
              for j in p.findall(str(content_class)):
                     j= j.replace('/', '.')
                     imple_interface3.append(j)
                     #print(imple_interface31)



              #------------------Subinterfaces:---------------------------------
              content_class = re.findall('<DT><B>All Known Subinterfaces:</B> <DD>(.*?)</DL>',interface_html,re.S)
              imple_interface31 = list()
              p = re.compile(r'<A HREF="../../(.*?).html">')
              for j in p.findall(str(content_class)):
                     j= j.replace('/', '.')
                     imple_interface31.append(j)
                     #print(imple_interface31)


              #------------------Implementing Classes:---------------------------------
              content_class = re.findall('<DT><B>All Known Implementing Classes:</B> <DD>(.*?)</DL>',interface_html,re.S)
              imple_class3 = list()
              p = re.compile(r'<A HREF="../../(.*?).html">')
              for j in p.findall(str(content_class)):
                     j= j.replace('/', '.')
                     imple_class3.append(j)
                     #print(imple_class3)


              #------------------Method Detail:---------------------------------
              content_methon = re.findall('<!-- ============ METHOD DETAIL ========== -->(.*?)<!-- ========= END OF CLASS DATA ========= -->',interface_html,re.S)
              content = str(content_methon)
              #print(content)
              menthon_list1 = list()
              p = re.compile(r'<PRE>(.*?)</PRE>',re.S)
              for j in p.findall(content):
                     #print(j)
                     menthon_list1.append(j)

              dict_method = dict()
              for x1 in range(len(menthon_list1)):
                     #print("Methon:")
                     methon = re.findall(r'<B>(.*?)</B>',menthon_list1[x1])
                     #print(methon)

                     
                     Parameter_type = re.findall(r'</B>\(<A HREF="../../(.*?).html">',menthon_list1[x1])
                     Parameter_type= str(Parameter_type).replace('/', '.')
                     Parameter_name = re.findall(r'</A>&nbsp;(.*?)\)',menthon_list1[x1])
                     
                     #print(Parameter_type)
                     #print(Parameter_name)
              
                     throw = re.findall(r'<B>Throws:</B><DD><CODE><A HREF="../../(.*?).html">',menthon_list1[x1])
                     throw= str(throw).replace('/', '.')
                     #print(throw)
                     
                     dict_method={"Methon":methon,"Parameter_name":Parameter_name,"Parameter_type":Parameter_type,"Throw":throw}
                     #dict_method[str(methon[0])]={"Parameter_name":Parameter_name,"Parameter_type":Parameter_type,"Throw":throw}
                     
              try:
                     result_dict[json_num] = merge(m2,m3,imple_interface3,imple_interface31,imple_class3,dict_method)
                     json_num+=1
              except:
                     continue
       with open("interface_result3.json","w") as f:
              json.dump(result_dict,f)
if __name__ == "__main__":
       main()
   

    
