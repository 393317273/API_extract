'''
对比两个版本的接口后输出一个结果文件
'''
#TODO: argv模块读取两个输入的版本号，然后读取这两个版本号的json文件
from utils import *
import sys
#TODO：根据全称对比
def main():
    if len(sys.argv)!=3:
        raise Exception('输入两个版本号')
    else:
        versionA,versionB = sys.argv[1:]
    JDKA = loadJson(getJsonPath(versionA))
    JDKB = loadJson(getJsonPath(versionB))
    #TODO：保证可读性的情况下，先返回接口的存在version和method的存在version