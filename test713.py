import json
import operator
def loadJson(path):
    with open(path,'r') as f:
        jsonDict = json.load(f)
    return jsonDict

def extractClass(jsonDict):
    #jsonDict就是JDK提取的json，另外建立一个字典专门存类，之后用set来处理
    classNames = []
    for __classId in jsonDict:
        classNames.append(str(jsonDict[__classId]["Class"]))
    return classNames

jdkPath = f".//class_result8.json"
jdkList = loadJson(jdkPath)
print(jdkList)






data=[
        {"name":"张三","age":18},{"name":"李四","age":20},
        {"name":"王五","age":19},{"name":"袁伟","age":17}
]
#reverse=True,降序，反之升序
sort_data=sorted(data, key=operator.itemgetter('age'), reverse=True)    
#print(sort_data)

