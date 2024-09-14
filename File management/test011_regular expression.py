'''
正则表达式
'''

import re

# search() 函数会在给定的字符串中搜索第一个与正则表达式模式匹配的部分。
# 如果找到匹配项，则返回一个匹配对象，该对象具有一些方法和属性，可以用于获取匹配的信息。如果没有找到匹配项，则返回 None。
matched = re.search(r"\w+?@\w+?\.com", "zsy1594577991@foxmail.com")
print("zsy1594577991@foxmail.com: ", matched)
matched = re.search(r"\w+?@\w+?\.com", "zsy1594577991@foxmail.com")
print("the email is zsy1594577991@fomail.com: ", matched)


