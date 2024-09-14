'''
正则表达式
'''

import re
found = []
for i in re.finditer(r"[\w-]+?\.jpg", "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jp "):
    #list.append(element)   list：要操作的列表对象   element：要添加到列表末尾的元素
    found.append(re.sub(r".jpg","", i.group()))
print(found)


print("***************************")


string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg, 2021-02-03.jpg"
print("without():", re.findall(r"[\w-]+?\.jpg", string))
#只要我们在正则表达中，加入一个 () 选定要截取返回的位置， 他就直接返回括号里的内容
print("with():", re.findall(r"([\w-]+?)\.jpg", string))


print("***************************")


string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-00000003.jpg"
match = re.finditer(r"(\d+?)-(\d+?)-(\d+?)\.jpg", string)

for file in match:
    #正则表达式模式 0+(\d{2}) 匹配了一个或多个连续的零，后跟两位数字。在替换中，我们使用了 \1 来引用正则表达式中的第一个捕获组（即两位数字
    all_fileter = re.sub(r"00+(\d{2})", r"\1", file.group())

    day_fileter = re.sub(r"0+", r"", file.group(3))
    print("matched string:", all_fileter, ",year:", file.group(1), ",month:", file.group(2),"day:", day_fileter)


print("***************************")


string = "I have 2021-01-01.jpg, 2022-02-02.jpg, 2023-03-03.jpg"
match = re.findall(r"(\d+?)-(\d+?)-(\d+?)\.jpg", string)
print(match)
for file in match:
    print("year:", file[0], "month:", file[1], "day:", file[2])


print("***************************")


#group("索引")索引，我们需要在括号中写上 ?P<索引名> 这种模式
string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
match = re.finditer(r"(?P<y>\d+)-(?P<m>\d+)-(?P<d>\d+)", string)
for file in match:
    print("matched_string:", file.group(),
          ",year:", file.group("y"),
          ",month:", file.group("m"),
          ", day:", file.group("d"))



print("**************************\n**多行匹配模式**\n**************************")
#多匹配模式


ptn, string = r"r[ua]n", "I Ran to you"
print("without re.I:", re.search(ptn, string))
print("with re.I:", re.search(ptn, string, flags=re.I))


ptn = r"^ran"
string = """I 
ran to you"""
print("without re.M:", re.search(ptn, string))
print("with re.M:", re.search(ptn, string, flags=re.M))
# re.match() 是不管你有没有 re.M flag，我的匹配都是按照最头头上开始匹配的
print("with re.M and match:", re.match(ptn, string, flags=re.M))


ptn = r"^ran"
string = """I
Ran to you"""
print("with re.M and re.I:", re.search(ptn, string, flags=re.M|re.I))
# 还有一种写法可以直接在 ptn 里面定义这些 flags
string = """I
Ran to you"""
re.search(r"(?im)^ran", string)



#更快的执行:提前compile字符串为正则表达式
import time
n = 1000000
string = "I ran to you"
t0 = time.time()
# 不提前 compile
for _ in range(n):
    re.search(r"ran", string)
t1 = time.time()
print("不提前compile的运行时间为：", t1-t0)

# 提前 compile
ptn = re.compile(r"ran")
for _ in range(n):
    ptn.search(string)
t2 = time.time()
print("提前compile的运行时间：", t2-t1)

print("提前compile比不提前compile快:", (t2-t1)-(t1-t0))












