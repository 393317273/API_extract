from urllib import response
import os
docPath = "C://Users//LGH//Desktop//APIdoc//jdk-17.0.3.1_doc-all//docs//api"      #"..//docs//api"       
#docPath = "..//docs//api"
docPath = os.path.abspath(docPath)#增加代码可复用性
all_class_link = []
for root, dirs, files in os.walk(docPath):
    for name in files:
        if root == docPath or name[-4:]!="html" :continue
        all_class_link.append(os.path.join(root, name).replace("\\","//"))