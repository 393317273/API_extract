import re
import urllib.request

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header()
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html

#p = re.compile(r'<a href=.*target="classFrame"', re.MULTILINE)

def get_class(html):
    p = r'<span class="interfaceName">(.*)</span>'
    classlist = re.findall(p,html)

    for each in classlist:
        print(each)

if __name__=='_main_':
    url = "file:///C:/docs/api/allclasses-frame.html"
    get_class(open_url(url))
   


  