import re
from unittest import result
from urllib import response


interface_html = '''
<li class="blockList">
<!-- ============ METHOD DETAIL ========== -->
<section role="region">
<ul class="blockList">
<li class="blockList"><a id="method.detail">
<!--   -->
</a><h3>Method Detail</h3>
<a id="topLevelWindowCreated(java.awt.Window)">
<!--   -->
</a>
<ul class="blockList">
<li class="blockList">
<h4>topLevelWindowCreated</h4>
<pre class="methodSignature">void&nbsp;topLevelWindowCreated&#8203;(<a href="../../../../../../java.desktop/java/awt/Window.html" title="class in java.awt">Window</a>&nbsp;w)</pre>
<div class="block">Invoked when a new top level window has been created.</div>
<dl>
<dt><span class="paramLabel">Parameters:</span></dt>
<dd><code>w</code> - the Window that was created</dd>
</dl>
</li>
</ul>
<a id="topLevelWindowDestroyed(java.awt.Window)">
<!--   -->
</a>
<ul class="blockListLast">
<li class="blockList">
<h4>topLevelWindowDestroyed</h4>
<pre class="methodSignature">void&nbsp;topLevelWindowDestroyed&#8203;(<a href="../../../../../../java.desktop/java/awt/Window.html" title="class in java.awt">Window</a>&nbsp;w)</pre>
<div class="block">Invoked when a top level window has been destroyed.</div>
<dl>
<dt><span class="paramLabel">Parameters:</span></dt>
<dd><code>w</code> - the Window that was destroyed</dd>
</dl>
</li>
</ul>
</li>
</ul>
</section>
</li>
</ul>
</div>
</div>
</main>'''

content_methon = re.findall('<h3>Method Detail</h3>(.*?)<!-- ========= END OF CLASS DATA ========= -->',interface_html,re.S)
content = str(content_methon)
menthon_list1 = list()
p = re.compile('<li class="blockList">(.*?)</li>',re.S)
for j in p.findall(content):
                     menthon_list1.append(j)
dict_method = dict()
for x1 in range(len(menthon_list1)):
                     #print("Methon:")
                     methon = re.findall(r'<h4>(.*?)</h4>',menthon_list1[x1])
                     print(methon)

                     #print("Parameter:")
                     Parameter_content1 = re.findall(r'<pre>.*\((.*?)\)',menthon_list1[x1])
                     #print(Parameter_content1)
                     Parameter = re.findall(r'title="class in(.*?)">(.*?)</a>&nbsp;(.*?)[)]</pre>',str(Parameter_content1))
                     print(Parameter)
                     
                     #print("Throw:")
                     throw_content = re.findall(r'<dt><span class="throwsLabel">(.*?)</dl>',menthon_list1[x1])
                     throw = re.findall(r'<dd><code><a href=".+">(.*?)</a></code>',str(throw_content))