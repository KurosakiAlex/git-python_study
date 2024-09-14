'''元组'''

t = ('zsy', 26, True, '东京')
print(t)
for n in t:
    print(n)

# 重新给元组赋值
# t[0] = '王大锤'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收

# 将元组转换成列表
lit = list(t)
print(lit)
# 列表是可以修改它的元素的
lit[0] = 'Alex'
print(lit)

# 将列表转换成元组
tuple_lit = tuple(lit)
print(tuple_lit)







