'''集合'''
# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 4, 5, 6}
print(set1)  #输出{1, 2, 3, 4, 5, 6}
print(len(set1))

# 创建集合的构造器语法
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 4, 5, 6, 7))
print(set2, set3)

# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)



# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
print(set2 - set1)
print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))

print("**************")

# 判断子集和超集
print(set1 <= set2)
# print(set2.issubset(set1))
print(set2 <= set1)
# print(set3.issubset(set1))
print(set1 >= set3)
# print(set1.issuperset(set2))
print(set2 >= set3)
# print(set1.issuperset(set3))










