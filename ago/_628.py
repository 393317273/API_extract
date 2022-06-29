import re
import urllib.request

interface_html='''<li class="blockList">
<dl>
<dt>All Superinterfaces:</dt>
<dd><a href="../../../org/omg/PortableServer/ServantManagerOperations.html" title="interface in org.omg.PortableServer">ServantManagerOperations</a></dd>
</dl>
<dl>
<dt>All Known Subinterfaces:</dt>
<dd><a href="../../../org/omg/PortableServer/ServantLocator.html" title="interface in org.omg.PortableServer">ServantLocator</a></dd>
</dl>
<dl>
<dt>All Known Implementing Classes:</dt>
<dd><a href="../../../org/omg/PortableServer/_ServantLocatorStub.html" title="class in org.omg.PortableServer">_ServantLocatorStub</a>, <a href="../../../org/omg/PortableServer/ServantLocatorPOA.html" title="class in org.omg.PortableServer">ServantLocatorPOA</a></dd>
</dl>'''

content_class = re.findall('<dt>All Known Implementing Classes:</dt>(.*?)</dl>',interface_html,re.S)
print(content_class)
imple_class1 = list()
p = re.compile(r'title="class in(.*?)">')
for j in p.findall(str(content_class)):
    imple_class1.append(j)
    #print(imple_class1[1])
content_class = re.findall('<dt>All Known Implementing Classes:</dt>(.*?)</dl>',interface_html,re.S)
imple_class2 = list()
p = re.compile(r'">(.+?)</a>')
for j in p.findall(str(content_class)):  
          imple_class2.append(j)
          #print(imple_class2[1])
print("implement classes:")
imple_class3 = list()
for l in range(len(imple_class1)):
           k = imple_class1[l] + '.' +imple_class2[l]
           imple_class3.append(k)
print(imple_class3)