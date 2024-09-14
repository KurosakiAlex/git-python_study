s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)



s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')


s1 = 'hello ' * 3
print(s1) # hello hello hello
print('ll' in s1) # True
print('good' in s1) # False

str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2])
print(str2[2:5])#前闭后开
print(str2[2:])
print(str2[::3])
print(str2[::2])
print(str2[::-1])
print(str2[-2:-4:-1])



str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
'''find 方法的返回值：
如果找到子字符串，则返回子字符串的第一个字符在原字符串中的索引。
如果未找到子字符串，则返回 -1。'''
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
print(str1.find('h')) # 0
# 与find类似但找不到子串时会引发异常
print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # Fals
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())
a, b = 5, 10
print(f'{a} * {b} = {a * b}')
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))
a, b = 5, 10
print(f'{a} * {b} = {a * b}')

# list
list1 = [1, 3, 5, 7, 100]
print(list1)
# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2)
# 计算列表长度(元素个数)
print(len(list2))
# 下标(索引)运算
print(list1[0])
print(list1[4])
# print(list1[5])  # IndexError: list index out of range
print(list1[-1])
list1[1] = 300
print(list1)
# 通过循环用下标遍历列表元素
print(len(list1))
print(range(len(list1)))
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)


# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
# 需要将所有偶数索引位置的元素修改为它们的平方
# 迭代
for index, elem in enumerate(list1):
    if index % 2 == 0:
        list1[index] = elem ** 2
print(list1)


str4 = '隔行符'
print(str4.center(50, '*'))

list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
print(list1)
list1.insert(1, 400)
print(list1)
# 合并两个列表
list1.extend([1000, 2000])
print(list1, len(list1))
if 3 in list1:
    list1.remove(3)
print(list1)
if 1234 in list1:
    list1.remove(1234)
print(list1)
# 从指定的位置删除元素
list1.pop(4)
print(list1)
list1.pop(len(list1) - 1)
print(list1)
# 清空列表元素
list1.clear()
print(list1)

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2) # apple strawberry waxberry
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4) # ['pitaya', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']

str4 = '隔行符'
print(str4.center(50, '*'))

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
print(list2)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用











