import json
versionA = 8
versionB = 9
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
对比两个类列表,B为更新的版本
'''
def compareClass(jdkA,jdkB):
    jdkA = set(jdkA)
    jdkB = set(jdkB)
    classAdded = jdkB - jdkA
    classDeprecated = jdkA - jdkB
    return (classAdded,classDeprecated)


def compareInterface(jdkA,jdkB):
    jdkA = set(jdkA)
    jdkB = set(jdkB)
    interfaceAdded = jdkB - jdkA
    interfaceDeprecated = jdkA - jdkB
    return (interfaceAdded,interfaceDeprecated)

def main():
    jdkAPath = f".//class_result{versionA}.json"
    jdkBPath = f".//class_result{versionB}.json"
    jdkAClassList,jdkBClassList = extractClass(loadJson(jdkAPath)), extractClass(loadJson(jdkBPath))
    classAdded,classDeprecated = compareClass(jdkAClassList,jdkBClassList)
    print("Class:")
    print(classAdded,classDeprecated)

    jdkAInterfaceList,jdkBInterfacesList = extractInterface(loadJson(jdkAPath)), extractInterface(loadJson(jdkBPath))
    interfaceAdded,interfaceDeprecated = compareInterface(jdkAInterfaceList,jdkBInterfacesList)
    print("Interface:")
    print(interfaceAdded,interfaceDeprecated)

if __name__ == "__main__":
    main()