from urllib.request import urlopen
import re

html = urlopen("https://mofanpy.com/static/scraping/basic-structure.html").read().decode('utf-8')

# 正则表达式匹配搜索
'''
(.+?) 是一个捕获组，表示匹配 <title> 和 </title> 标签之间的所有字符：
. 匹配任意字符（除换行符）。
+ 表示匹配前面的字符一次或多次。
? 使 + 成为非贪婪模式，尽可能少地匹配字符。
'''

# 找一找所有的链接
'''
href="，这是 HTML 标签中属性的开始部分。
'''
res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)
res01 = re.findall(r'href=["\'](.*?)["\']', html)
print("\nAll links: ", res01)
print(html[:1000])