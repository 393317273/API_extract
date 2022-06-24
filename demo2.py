#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint
import re
from urllib import response
import urllib.request


html = '''<h2 title="Interfaces">Interfaces</h2>
<ul title="Interfaces">
<li><a href="AttributeList.html" title="interface in org.xml.sax" target="classFrame"><span class="interfaceName">AttributeList</span></a></li>
<li><a href="Attributes.html" title="interface in org.xml.sax" target="classFrame"><span class="interfaceName">Attributes</span></a></li>
<li><a href="ContentHandler.html" title="interface in org.xml.sax" target="classFrame"><span class="interfaceName">ContentHandler</span></a></li>
<li><a href="DocumentHandler.html" title="interface in org.xml.sax" target="classFrame"><span class="interfaceName">DocumentHandler</span></a></li>
<li><a href="DTDHandler.html" title="interface in org.xml.sax" target="classFrame"><span class="interfaceName">DTDHandler</span></a></li>
<li><a href="EntityResolver.html" title="interface in org.xml.sax" target="classFrame"><span class="interfaceName">EntityResolver</span></a></li>
<li><a href="ErrorHandler.html" title="interface in org.xml.sax" target="classFrame"><span class="interfaceName">ErrorHandler</span></a></li>
<li><a href="Locator.html" title="interface in org.xml.sax" target="classFrame"><span class="interfaceName">Locator</span></a></li>
<li><a href="Parser.html" title="interface in org.xml.sax" target="classFrame"><span class="interfaceName">Parser</span></a></li>
<li><a href="XMLFilter.html" title="interface in org.xml.sax" target="classFrame"><span class="interfaceName">XMLFilter</span></a></li>
<li><a href="XMLReader.html" title="interface in org.xml.sax" target="classFrame"><span class="interfaceName">XMLReader</span></a></li>
</ul>
<h2 title="Classes">Classes</h2>
<ul title="Classes">
<li><a href="HandlerBase.html" title="class in org.xml.sax" target="classFrame">HandlerBase</a></li>
<li><a href="InputSource.html" title="class in org.xml.sax" target="classFrame">InputSource</a></li>
</ul>'''


content = re.findall('<ul title="Classes">(.*?)</ul>',html,re.S)
p = re.compile(r'target="classFrame">(.*?)</a>')
for j in p.findall(str(content)):
    classlist = list()
    classlist.append(j)
    print(classlist)#输出Class


    

