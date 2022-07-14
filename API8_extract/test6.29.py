from asyncio.windows_events import NULL
from contextlib import nullcontext
import re
from urllib import response
import urllib.request
class_html='''<!-- =========== FIELD SUMMARY =========== -->
<ul class="blockList">
<li class="blockList"><a name="field.summary">
<!--   -->
</a>
<h3>Field Summary</h3>
<table class="memberSummary" border="0" cellpadding="3" cellspacing="0" summary="Field Summary table, listing fields, and an explanation">
<caption><span>Fields</span><span class="tabEnd">&nbsp;</span></caption>
<tr>
<th class="colFirst" scope="col">Modifier and Type</th>
<th class="colLast" scope="col">Field and Description</th>
</tr>
<tr class="altColor">
<td class="colFirst"><code>static int</code></td>
<td class="colLast"><code><span class="memberNameLink"><a href="../../java/lang/Byte.html#BYTES">BYTES</a></span></code>
<div class="block">The number of bytes used to represent a <code>byte</code> value in two's
 complement binary form.</div>
</td>
</tr>
<tr class="rowColor">
<td class="colFirst"><code>static byte</code></td>
<td class="colLast"><code><span class="memberNameLink"><a href="../../java/lang/Byte.html#MAX_VALUE">MAX_VALUE</a></span></code>
<div class="block">A constant holding the maximum value a <code>byte</code> can
 have, 2<sup>7</sup>-1.</div>
</td>
</tr>
<tr class="altColor">
<td class="colFirst"><code>static byte</code></td>
<td class="colLast"><code><span class="memberNameLink"><a href="../../java/lang/Byte.html#MIN_VALUE">MIN_VALUE</a></span></code>
<div class="block">A constant holding the minimum value a <code>byte</code> can
 have, -2<sup>7</sup>.</div>
</td>
</tr>
<tr class="rowColor">
<td class="colFirst"><code>static int</code></td>
<td class="colLast"><code><span class="memberNameLink"><a href="../../java/lang/Byte.html#SIZE">SIZE</a></span></code>
<div class="block">The number of bits used to represent a <code>byte</code> value in two's
 complement binary form.</div>
</td>
</tr>
<tr class="altColor">
<td class="colFirst"><code>static <a href="../../java/lang/Class.html" title="class in java.lang">Class</a>&lt;<a href="../../java/lang/Byte.html" title="class in java.lang">Byte</a>&gt;</code></td>
<td class="colLast"><code><span class="memberNameLink"><a href="../../java/lang/Byte.html#TYPE">TYPE</a></span></code>
<div class="block">The <code>Class</code> instance representing the primitive type
 <code>byte</code>.</div>
</td>
</tr>
</table>
</li>
</ul>'''
content_filed =re.findall('<h3>Field Summary</h3>(.*?)</table>',class_html,re.S) 
content1 = str(content_filed)
field_list1 = list()
p = re.compile('<td class="colFi(.*?)</tr>',re.S)
for j in p.findall(content1):
        field_list1.append(j)
dict_field = dict()
for x1 in range(len(field_list1)):
        field_name = re.findall(r'<td class="colLast"><code><span class="memberNameLink"><a href=".*">(.*?)</a></span></code>',field_list1[x1])
        #print(field_name[0])
        Modifier = re.findall(r'st"><code>(.*?) <a href',str(field_list1[x1]))
        type1 = re.findall(r'<a href.*" title="class in (.*?)">',str(field_list1[x1]))
        type2 = re.findall(r'st"><code>.* <a href.*" title="class in .*">(.*?)</a></code></td>',str(field_list1[x1]))
        if len(type1)==0:
            type=type2
        else:
            type = ''.join(type1)+'.'+''.join(type2)                 
        #type = re.findall(r'st"><code>(.*?) <a href.*" title="class in (.*?)">(.*?)</a></code></td>',str(field_list1[x1]))
#print(type)                
#dict_field1 = dict()
dict_field = {"Modifier":Modifier,"Type":type,"Field_name":field_name}
#dict_method[str(methon[0])] = {"Parameter":Parameter,"Throw":throw}
#dict_field[str(field_name[0])] = {"Type":type}
print(dict_field)



 