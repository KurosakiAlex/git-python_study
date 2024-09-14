'''
正则表达式
'''
import re

#方法一
matched = re.search(r"run|ran", "I want to run")
print(matched)

#方法二
matched00 = re.search(r"r[au]n", "I want to run")
print(matched00)

#同时满足多个字符的不同匹配          注意小括号
matched01 = re.search(r"F(i|ou)nd", "I Found you")
matched02 = re.search(r"F(ou|i)nd", "I Find you")
print(matched01)
print(matched02)




#{8}表示前面的 模式（\d）必须连续重复匹配 8 次
print(re.search(r"070\d{8}","07093030541"))
print(re.search(r"070\d{8}", "07093030541123456789"))




#中文
print(re.search(r"不?爱", "我爱你"))
print(re.search(r"不?爱", "我不爱你"))
print(re.search(r"不.*?爱", "我不讨厌你，我是很爱爱爱爱爱你"))

#这个符号修饰前面的字符
#有?这个贪婪字符就是最小匹配次数，没有?这个贪婪字符就是最大匹配次数
print(re.search(r"不+爱", "不不爱讨厌你，我是很爱爱爱你爱"))
print(re.search(r"不+?爱", "不不爱讨厌你，我是很爱爱爱你爱"))





zhong = "中".encode("unicode-escape")
print(zhong)

#用Unicode过滤中文
unicoded01 = re.search(r"[\u4e00-\u9fa5]+", "你好兄弟萌，Hello our friends!")
print(unicoded01)
#留下对标点符号的识别
unicoded02 = re.search(r"[\u4e00-\u9fa5！？。，￥【】「」]+", "你好兄弟萌，Hello our friends！")
print(unicoded02)




print("************************************************************")
#查找替换等更多功能
print("search:", re.search(r"run", "I run to you"))
print("match:", re.match(r"run", "I run to you"))
print("findall:", re.findall(r"r[ua]n", "I run to you. you ran to him"))

for i in re.finditer(r"r[ua]n", "I run to you. you ran to him"):
    print("finditer:", i)

print("split:", re.split(r"r[ua]n", "I run to you. you ran to him"))
print("sub:", re.sub(r"r[ua]n", "jump", "I run to you. you ran to him"))
print("subn:", re.subn(r"r[ua]n", "jump", "I run to you. you ran to him"))




#for遇到可以迭代的数据结构就可以自动实现迭代
shit_mountain = [1, 2, 3., "a", {"k", "v"}]

for idx in range(len(shit_mountain)):
    print(shit_mountain[idx])
print(list(range(5)))

#for遇到可以迭代的数据结构就可以自动实现迭代
for shit in shit_mountain:
    print("now shit should be:",shit)

shit_iter = iter(shit_mountain)
print(shit_iter.__next__())
print(shit_iter.__next__())
print(shit_iter.__next__())
print(shit_iter.__next__())
print(shit_iter.__next__())
print(shit_iter.__next__())


