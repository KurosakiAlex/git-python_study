'''
莫烦python学习
https://mofanpy.com/tutorials/python-basic/interactive-python/var-ops-print

'''


long_test = """
这是一段
文本
用来证明三个双引号可以跨行
书写的文本
"""

print('********************************')


name1, name2, name3 = "文件", "系统", "内核"
name4 = name1 + name2

print(long_test)
print(name3)

# 字符串也是可以加起来的
print(name4)


print('********************************')

def test(a):
    a += 1
    return a


print(test(1))

















