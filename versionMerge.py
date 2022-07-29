'''
对比两个版本的接口后输出一个结果文件
'''
merged_path = "interface_merged.json"
#DONE: argv模块读取两个输入的版本号，然后读取这两个版本号的json文件

from utils import *
import sys
#DONE：根据全称对比
#TODO：为了将所有一起对比，进行递归化
#每一层独立读取版本，只输入版本号，不然太麻烦
def Merge_Recursive(versionA,versionB_merge):
    if len(versionB_merge) == 1:
        versionB = versionB_merge[0]
        #递归最里层
        JDKA = extractFullInterface(loadJson(getJsonPath(versionA),versionA))
        JDKB = extractFullInterface(loadJson(getJsonPath(versionB),versionB))
        JDK_merged = compareJDK(JDKA,JDKB,versionA,versionB)
        return JDK_merged
    else:
        #每次以最左边一个版本号为A，剩下的全作为B
        __versionA = versionB_merge[0]
        __versionB = versionB_merge[1:]
        JDKB = Merge_Recursive(__versionA,__versionB)
        JDKA = extractFullInterface(loadJson(getJsonPath(versionA),versionA))
        JDK_merged = compareJDK(JDKA,JDKB,versionA,versionB_merge)
        return JDK_merged
def main():
    if len(sys.argv)!=3:
        raise Exception('输入两个版本号')
    else:
        versionA,versionB = sys.argv[1:]
    JDKA = loadJson(getJsonPath(versionA),versionA)
    JDKB = loadJson(getJsonPath(versionB),versionB)
    #TODO：保证可读性的情况下，先返回接口的存在version和method的存在version
    JDKA_full = extractFullInterface(JDKA)
    JDKB_full = extractFullInterface(JDKB)
    JDK_merged = compareJDK(JDKA_full,JDKB_full,versionA,versionB)
    writeJson(JDK_merged,merged_path)
def testRecursive():
    #TODO:递归中因为写法问题，只存在于新版本的API版本号回直接变成整个versionB的，修复
    Version_List = [8,9,11]
    result = Merge_Recursive(Version_List[0],Version_List[1:])
    writeJson(result,"fullMergeTest.json")
if __name__ == "__main__":
    testRecursive()