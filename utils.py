from bs4 import BeautifulSoup as bs, NavigableString
import json
import re
#from types import NoneType
def loadJson(path,version):
    with open(path,'r') as f:
        jsonDict = json.load(f)
    jsonDict["version"] = version
    return jsonDict
def writeJson(jsonDict,path):
    with open(path,'w') as f:
        json.dump(jsonDict,f)
'''
提取字典里的class全名
'''
def extractClass(jsonDict):
    #jsonDict就是JDK提取的json，另外建立一个字典专门存类，之后用set来处理
    classNames = []
    for __classId in jsonDict:
        classNames.append(str(jsonDict[__classId]["Class"]))
    return classNames

def extractInterface(jsonDict):
    
    interfaceNames = []
    for __interfaceId in jsonDict:
        interfaceNames.append(str(jsonDict[__interfaceId]["Package"]))
    return interfaceNames
'''
输入json版本号，拼接得到当前目录存储了对应JDK版本数据的文件的路径
'''
def getJsonPath(jsonVer):
    return f"interface_result{jsonVer}.json"

#DONE:两个功能 注意为了可读性，把全称作为键名返回吧
'''
输入JDK字典，拼接并返回所有接口的全名，返回以全称作为建名的字典
'''
def extractFullInterface(jsonDict):
    newJDKDict = {}
    for __classId in jsonDict:
        if __classId == "version":
            continue
        newJDKDict[f"{jsonDict[__classId]['Package']}.{jsonDict[__classId]['Interface']}"] = jsonDict[__classId]
    return newJDKDict
#DEPRECATED: 将函数改为可递归（versionB可能含有多个版本信息）
'''
输入两个method字典，整合并输出一个带有version键值对的字典
'''
#DONE: 修复格式问题以匹配字典数组
#TODO: 可能存在的问题：同名method可能无法判断出哪个亚种是先出现的,这会是个问题。最好加上参数个数匹配，
#TODO: 在递归过程中，因为会把existed_version这个键也放了进去，导致会出现重复现象
def compareMethod(methodDictA,methodDictB,versionA,versionB):
    mergedMethod = {}
    A_method = [str(x) for x in methodDictA] #将整个字典转成字符串试试
    B_method = [str(x) for x in methodDictB]
    mergedMethodList = list()
    for method in list(set(A_method)-set(B_method)):
        mergedMethodList.append(eval(method))
        mergedMethodList[-1][list(eval(method).keys())[0]]["Exist_Version"] = [versionA]
    for method in list(set(B_method)-set(A_method)):
        mergedMethodList.append(eval(method))
        if isinstance(versionB,int):
            mergedMethodList[-1][list(eval(method).keys())[0]]["Exist_Version"] = [versionB]
        else:
            mergedMethodList[-1][list(eval(method).keys())[0]]["Exist_Version"] = versionB
    for method in list(set(B_method) & set(A_method)):
        mergedMethodList.append(eval(method))
        if isinstance(versionB,int):
            mergedMethodList[-1][list(eval(method).keys())[0]]["Exist_Version"] = [versionA,versionB]
        else:
            mergedMethodList[-1][method]["Exist_Version"] = [versionA]+versionB
    return mergedMethodList
'''
输入两个JDK字典，用桶排序遍历键名，查询只在18出现的，两者皆有的，只在19出现的，然后返回
'''
# 如果输入的版本B是一个数组，JDKB也是经过合并处理的，你要怎么弄？
# DONE:2022-8-19：修复索引问题
def compareJDK(JDKA,JDKB,A_version,B_version):
    mergedJDK = {}
    JDKA_interface = JDKA.keys()
    JDKB_interface = JDKB.keys()
    # 对比类
    interfaceOnlyinB = set(JDKB_interface) - set(JDKA_interface)
    interfaceOnlyinA = set(JDKA_interface) - set(JDKB_interface)
    interfaceinBoth = set(JDKA_interface) & set(JDKB_interface)
    # 对比方法 只对均出现的接口方法进行方法对比即可
    
    for interface in list(interfaceOnlyinA):
        mergedJDK[interface] = JDKA[interface]
        mergedJDK[interface]["Exist_Version"] = [A_version]
        # 根据修改后的数据结构，methodName是一个字典列表，下面的逻辑都需要重新整理
        methodIndice = 0 #每个接口是独有一个字典列表，所以索引下标每次在此重置
        for methodDict in mergedJDK[interface]["Method"]:
            # DONE: 要想一个办法 对应到list里的字典对象
            
            mergedJDK[interface]["Method"][methodIndice][list(methodDict.keys())[0]]["Exist_Version"] = [A_version]
            methodIndice += 1
    for interface in list(interfaceOnlyinB):
        mergedJDK[interface] = JDKB[interface]
        if isinstance(B_version,int):
            mergedJDK[interface]["Exist_Version"] = [B_version]
        else:
            mergedJDK[interface]["Exist_Version"] = JDKB[interface]["Exist_Version"] 
        methodIndice = 0 #每个接口是独有一个字典列表，所以索引下标每次在此重置
        for methodDict in mergedJDK[interface]["Method"]:
            if isinstance(B_version,int):
                mergedJDK[interface]["Method"][methodIndice][list(methodDict.keys())[0]]["Exist_Version"] = [B_version]         
            else:
                mergedJDK[interface]["Method"][methodIndice][list(methodDict.keys())[0]]["Exist_Version"] = JDKB[interface]["Method"][methodIndice][list(methodDict.keys())[0]]["Exist_Version"]
            methodIndice += 1
    for interface in list(interfaceinBoth):
        mergedJDK[interface] = JDKA[interface]
        if isinstance(B_version,int):
            mergedJDK[interface]["Exist_Version"] = [A_version,B_version]
        else:
            mergedJDK[interface]["Exist_Version"] = [A_version]+JDKB[interface]["Exist_Version"]
        mergedMethod = compareMethod(JDKA[interface]["Method"],JDKB[interface]["Method"],A_version,B_version)
        mergedJDK[interface]["Method"] = mergedMethod
    return mergedJDK

#TODO:2022-8-20发现 getValues​(List<? extends Field> fields)这样的提取不出来
def detectFullParams(HTMLstring,methon):
    #TODO:干脆全部都在pre里面提取，提取完参数类型提取参数得了
    params = {}
    soup = bs(HTMLstring,'html.parser',from_encoding='utf-8')
    try:
        paramContainer_Mid = soup.pre.contents
        paramContainer = [str(x) for x in paramContainer_Mid]
        fullContent =''.join([x for x in ' '.join(paramContainer).replace('\xa0',' ') if x.isprintable()])#去除一系列不可见字符并保留空格
        #isprintable()如果字符串的所有字符都是可打印的，则isprintable()方法在其他所有情况下返回true，则返回true
        #print(fullContent)
        methodContent = re.findall(rf'{methon[0]}(\(.*?\))',fullContent)[0].split('\\n')
        #按换行符split并在for中分别做成soup
        if methodContent[0] == '()':
            return params 
        for methodSentence in methodContent:
            methodSoup = bs(methodSentence,'html.parser',from_encoding='utf-8')
            if not isinstance(methodSoup.a,type(None)):
                #这一行有a，就是有超链接指向的非自定义类型
                methodType = str(methodSoup.a.next)
                methodName = str(methodSoup.a.next.next)
                methodName = ''.join([x for x in methodName if x.isalpha()])
             #isalpha()方法:判断字符串是否只由字母组成,如果字符串中所有字符都是字母则返回True,否则返回False   
                
            else:
                #这一行没a 内置数据类型
                (methodType,methodName) = [x for x in methodSentence.split(' ') if x!='']
                methodType = ''.join([x for x in methodType if x.isalpha()])
                methodName = ''.join([x for x in methodName if x.isalpha()])
            params[methodName] = methodType
        
        #type1:<pre><a href="../../java/awt/PaintContext.html" title="interface in java.awt">PaintContext</a> 
        # createContext(<a href="../../java/awt/image/ColorModel.html" title="class in java.awt.image">ColorModel</a> cm,\n                           
        # <a href="../../java/awt/Rectangle.html" title="class in java.awt">Rectangle</a> deviceBounds,\n                           
        # <a href="../../java/awt/geom/Rectangle2D.html" title="class in java.awt.geom">Rectangle2D</a> userBounds,\n                           
        # <a href="../../java/awt/geom/AffineTransform.html" title="class in java.awt.geom">AffineTransform</a> xform,\n                           
        # <a href="../../java/awt/RenderingHints.html" title="class in java.awt">RenderingHints</a> hints)</pre>
        #type2:<pre>void setMaximum(int max)</pre>
        #先做成soup检测有没有a标签，有的话优先提出来，再去处理剩下的
        return params
    except AttributeError:
        return params


def detectFullParams2(HTMLstring,methon):
    params = {}
    #soup = bs(HTMLstring,'html.parser',from_encoding='utf-8')
    try:        
        paramContainer = re.findall(r'<span class="parameters">(.*?)</span>',HTMLstring)
        if(paramContainer):
            fullContent =''.join([x for x in ' '.join(paramContainer).replace('&nbsp;',' ') if x.isprintable()])#去除一系列不可见字符并保留空格
            #print(fullContent)
            methodContent = fullContent.split('\\n')
            #print(methodContent)
            if methodContent[0] == '()':
                return params
            for methodSentence in methodContent:
                methodSoup = bs(methodSentence,'html.parser',from_encoding='utf-8')
                #print(methodSentence)
                if not isinstance(methodSoup.a,type(None)):
                    #这一行有a，就是有超链接指向的非自定义类型
                    methodType = str(methodSoup.a.next)
                    methodName = str(methodSoup.a.next.next)
                    methodName = ''.join([x for x in methodName if x.isalpha()])
                #isalpha()方法:判断字符串是否只由字母组成,如果字符串中所有字符都是字母则返回True,否则返回False   
                    
                else:
                    #这一行没a 内置数据类型
                    (methodType,methodName) = [x for x in methodSentence.split(' ') if x!='']
                    methodType = ''.join([x for x in methodType if x.isalpha()])
                    methodName = ''.join([x for x in methodName if x.isalpha()])
                params[methodName] = methodType
        return params
    except AttributeError:
        return params

#type1:(<a href="../../../../../java.base/java/lang/String.html" title="class in java.lang">String</a>&nbsp;title,
#      \n <a href="../../../../../java.base/java/lang/String.html" title="class in java.lang">String</a>&nbsp;media)
#type2:(int&nbsp;tabIndex)
#type3:(<a href="../../../../../java.base/java/lang/String.html" title="class in java.lang">String</a>&nbsp;target)
#type4:(short&nbsp;stringType,\n <a href="../../../../../java.base/java/lang/String.html" title="class in java.lang">String</a>&nbsp;stringValue)
   