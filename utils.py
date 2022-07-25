import json
def loadJson(path):
    with open(path,'r') as f:
        jsonDict = json.load(f)
    return jsonDict
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

#TODO:两个功能
'''
输入JDK字典，拼接并返回所有接口的全名，返回两个字典：一个存了全名的，一个只有Interface的
'''
def extractFullInterface(jsonDict):
    pass
#TODO：能不能用set来解决字典取并集的问题？感觉要用递归的办法 先实现了interface跟method的比对再说
'''
输入JDK字典，返回只存了全名和method的
'''
def extractMethod(jsonDict):
    pass