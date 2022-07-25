from heapq import merge
import json
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
'''
输入两个method字典，整合并输出一个带有version键值对的字典
'''
def compareMethod(methodDictA,methodDictB,versionA,versionB):
    mergedMethod = {}
    A_method = methodDictA.keys()
    B_method = methodDictB.keys()
    for method in list(set(A_method)-set(B_method)):
        mergedMethod[method] = methodDictA[method]
        mergedMethod[method]["Exist_Version"] = versionA
    for method in list(set(B_method)-set(A_method)):
        mergedMethod[method] = methodDictB[method]
        mergedMethod[method]["Exist_Version"] = versionB
    for method in list(set(B_method) & set(A_method)):
        mergedMethod[method] = methodDictA[method]
        mergedMethod[method]["Exist_Version"] = f"{versionA},{versionB}"
    return mergedMethod
'''
输入两个JDK字典，用桶排序遍历键名，查询只在18出现的，两者皆有的，只在19出现的，然后返回
'''
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
        mergedJDK[interface]["Exist_Version"] = A_version
        for methodName in mergedJDK[interface]["Method"]:
            mergedJDK[interface]["Method"][methodName]["Exist_Version"] = A_version
    for interface in list(interfaceOnlyinB):
        mergedJDK[interface] = JDKB[interface]
        mergedJDK[interface]["Exist_Version"] = B_version
        for methodName in mergedJDK[interface]["Method"]:
            mergedJDK[interface]["Method"][methodName]["Exist_Version"] = B_version         
    for interface in list(interfaceinBoth):
        mergedJDK[interface] = JDKA[interface]
        mergedJDK[interface]["Exist_Version"] = f"{A_version},{B_version}"
        mergedMethod = compareMethod(JDKA[interface]["Method"],JDKB[interface]["Method"],A_version,B_version)
        mergedJDK[interface]["Method"] = mergedMethod
    return mergedJDK
