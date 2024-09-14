'''
正则表达式
'''

import re

#r 代表原生字符串， 使用 r 开头的字符串是为了不让你混淆 pattern 字符串中到底要写几个 \，你只要当成一个规则来记住在写 pattern 的时候，都写上一个 r 在前面就好了。
match = re.search(r"run", "I run to you")
print(match)

#group() 能取出来里面找到的字符。 我们后面在详细介绍 group 的功能。
print(match.group())


# 上面那一句和下面这一句效果一样
print(re.search(r"run", "I run to you").group())


