from selenium import webdriver
import urllib.request
from urllib.request import URLError
import time

# 调用chrome浏览器并后台运行
option=webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(options=option)

# driver = webdriver.Chrome()
driver.get("file:///C:/docs/api/overview-frame.html")   # 要测试的页面
urls = driver.find_elements_by_xpath("//a")   # 匹配出所有a元素里的链接
print("该网页一共有%d个链接："%len(urls))

success_count = 0
fail_count = 0
for url in urls:
    real_url = url.get_attribute('href')
    if real_url == 'None':   # 很多的a元素没有链接，所以是None
        continue
    try:
        response = urllib.request.urlopen(real_url)   # 可以通过urllib测试url地址是否能打开
        time.sleep(1)

    except URLError as reason:
        fail_count += 1
        print('问题链接%d显示的是:'%fail_count, real_url, '对应的文本是：' + url.get_attribute("text"))   # 把测试不通过的url显示出来
    else:
        success_count += 1
        print('可用链接%d是:'%success_count, real_url)   # 测试通过的url展示出来

driver.close()
