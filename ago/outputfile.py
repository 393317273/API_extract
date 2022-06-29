def lgh():
    list = ['1','2','3']
    print(list)

with open('C:/Users/LGH/Desktop/API_extract.txt', 'a+') as f:
    print(lgh(), file=f)

# 将数据输出文件中，注意点1. 所指定的盘存在，2. 使用file=
'''fp = open("G:/Codes/test1.text", "a+")  # a+ 如果文件不存在就创建。存在就在文件内容的后面继续追加
print("我打印成功了！", file=fp)
fp.close()'''
