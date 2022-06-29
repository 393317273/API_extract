from urllib import response
import os
docPath = "..//docs//api"
all_interface_link = []
for root, dirs, files in os.walk(docPath):
    for name in files:
        if root == docPath or name[-4:]!="html" :continue
        all_interface_link.append(os.path.join(root, name).replace("\\","//"))
