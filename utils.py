from types import NoneType
from bs4 import BeautifulSoup as bs, NavigableString
import json
import re
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

#TODO:两个功能 注意为了可读性，把全称作为键名返回吧
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
#TODO: 将函数改为可递归（versionB可能含有多个版本信息）
'''
输入两个method字典，整合并输出一个带有version键值对的字典
'''
def compareMethod(methodDictA,methodDictB,versionA,versionB):
    mergedMethod = {}
    A_method = methodDictA.keys()
    B_method = methodDictB.keys()
    for method in list(set(A_method)-set(B_method)):
        mergedMethod[method] = methodDictA[method]
        mergedMethod[method]["Exist_Version"] = [versionA]
    for method in list(set(B_method)-set(A_method)):
        mergedMethod[method] = methodDictB[method]
        if isinstance(versionB,int):
            mergedMethod[method]["Exist_Version"] = [versionB]
        else:
            mergedMethod[method]["Exist_Version"] = methodDictB[method]["Exist_Version"]
    for method in list(set(B_method) & set(A_method)):
        mergedMethod[method] = methodDictA[method]
        if isinstance(versionB,int):
            mergedMethod[method]["Exist_Version"] = [versionA,versionB]
        else:
            mergedMethod[method]["Exist_Version"] = [versionA]+methodDictB[method]["Exist_Version"]
    return mergedMethod
'''
输入两个JDK字典，用桶排序遍历键名，查询只在18出现的，两者皆有的，只在19出现的，然后返回
'''
# 如果输入的版本B是一个数组，JDKB也是经过合并处理的，你要怎么弄？
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
        for methodName in mergedJDK[interface]["Method"]:
            mergedJDK[interface]["Method"][methodName]["Exist_Version"] = [A_version]
    for interface in list(interfaceOnlyinB):
        mergedJDK[interface] = JDKB[interface]
        #TODO:把len法改成判断数据类型
        if isinstance(B_version,int):
            mergedJDK[interface]["Exist_Version"] = [B_version]
        else:
            mergedJDK[interface]["Exist_Version"] = JDKB[interface]["Exist_Version"] 
        for methodName in mergedJDK[interface]["Method"]:
            if isinstance(B_version,int):
                mergedJDK[interface]["Method"][methodName]["Exist_Version"] = [B_version]         
            else:
                mergedJDK[interface]["Method"][methodName]["Exist_Version"] = JDKB[interface]["Method"][methodName]["Exist_Version"]
    for interface in list(interfaceinBoth):
        mergedJDK[interface] = JDKA[interface]
        if isinstance(B_version,int):
            mergedJDK[interface]["Exist_Version"] = [A_version,B_version]
        else:
            mergedJDK[interface]["Exist_Version"] = [A_version]+JDKB[interface]["Exist_Version"]
        mergedMethod = compareMethod(JDKA[interface]["Method"],JDKB[interface]["Method"],A_version,B_version)
        mergedJDK[interface]["Method"] = mergedMethod
    return mergedJDK

def detectParam(HTMLstring,methon):
    soup = bs(HTMLstring,'html.parser',from_encoding='utf-8')
    print(soup.prettify())
    #TODO:把param type也顺便检测了吧    
    #参数类型在这段中的pre标签可以找到，建议调试看看出来个啥
    #并不是所有数据类型都会被a标签包裹,比如int类型，这些要另外想办法。
    #type1:<pre><a href="../../java/awt/PaintContext.html" title="interface in java.awt">PaintContext</a> 
    # createContext(<a href="../../java/awt/image/ColorModel.html" title="class in java.awt.image">ColorModel</a> cm,\n                           
    # <a href="../../java/awt/Rectangle.html" title="class in java.awt">Rectangle</a> deviceBounds,\n                           
    # <a href="../../java/awt/geom/Rectangle2D.html" title="class in java.awt.geom">Rectangle2D</a> userBounds,\n                           
    # <a href="../../java/awt/geom/AffineTransform.html" title="class in java.awt.geom">AffineTransform</a> xform,\n                           
    # <a href="../../java/awt/RenderingHints.html" title="class in java.awt">RenderingHints</a> hints)</pre>
    #type2:<pre>void setMaximum(int max)</pre>
    #获取pre标签，匹配并取出函数名和完整形参列表
    #三种情况：只有a标签，完全没有a标签，二者混杂
    Parameters = []
    params = {}
    try:
        if soup.span.attrs['class'][0] == "paramLabel":

            iterateStart_Point = soup.span.previous_element.next_siblings #跳出span，从dt的下一个兄弟节点开始遍历 用next_siblings方法构建遍历器
            for sibling in iterateStart_Point:
                if isinstance(sibling,NavigableString):continue #换行符跳过
                if sibling.name == "dt":break # 到下一个包裹了span的dt，可能是return也可能是throw，就直接跳出
                if sibling.name == "dd":
                    param = sibling.code.string # dd块里的第一个code包裹的就是param
                    Parameters.append(param)
        #先获取函数名与完整形参列表
        #fullMethod = str(soup.find(string = re.compile(f"{methon}\((.*?)\)"))).split("(")[1][:-1].replace(u'\xa0', u' ')
        fullMethod = soup.pre.contents
        if len(Parameters) != 0:
            for param in Parameters:
                for i in range(len(fullMethod)):
                    if len(re.find(f'{param}',fullMethod[i]))!=0:
                        #你这么匹配会不会遇上误匹配的情况？比如另一个param包含了此param的全部字符
                        params[f'{param}'] = fullMethod[i-1]
        return Parameters
    except (AttributeError,IndexError): #不存在params的情况
        return Parameters

def detectFullParams(HTMLstring,methon):
    #TODO:干脆全部都在pre里面提取，提取完参数类型提取参数得了
    params = {}
    soup = bs(HTMLstring,'html.parser',from_encoding='utf-8')
    paramContainer_Mid = soup.pre.contents
    paramContainer = [str(x) for x in paramContainer_Mid]
    fullContent = ' '.join(paramContainer)
    fullContent = str(fullContent).replace(u'\xa0', u' ')
    #print(fullContent)
    methodContent = re.findall(rf'{methon[0]}(\(.*?\))',fullContent)[0].split('\\n')
    #按换行符split并在for中分别做成soup
    if methodContent[0] == '()':
        return params
    for methodSentence in methodContent:
        methodSoup = bs(methodSentence,'html.parser',from_encoding='utf-8')
        if not isinstance(methodSoup.a,NoneType):
            #这一行有a，就是有超链接指向的非自定义类型
            methodType = str(methodSoup.a.next)
            methodName = str(methodSoup.a.next.next)
            methodName = ''.join([x for x in methodName if x.isalpha()])
            
            
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




