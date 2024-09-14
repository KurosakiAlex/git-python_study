'''字典'''

# 创建字典的字面量语法
score = {'令狐冲' : 25, '张无忌' : 35, '郭靖' : 45}
print(score)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
print(items1)

# 通过zip函数将两个序列压成字典
a = ['a', 'b', 'c']
b = '123'
items = zip(a, b)
print(items)
items2 = dict(zip(a, b))
print(items2)

# 创建字典的推导式语法
items3 = {num : num**2 for num in range(1, 5)}
print(items3)

# 通过键可以获取字典中对应的值
print(score['张无忌'])
# 对字典中所有键值对进行遍历
for n in score:
    print(f'{n}:{score[n]}')
# 更新字典中的元素
score['郭靖'] = 65
score['诸葛王朗'] = 71
score.update(冷面=67, 方启鹤=85)
print(score)
if '令狐冲' in score:
    print(score['令狐冲'])
print(score.get('令狐冲'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(score.get('令狐冲', 20))
# 删除字典中的元素
print(score.popitem())
print(score.popitem())
print(score)
print(score.pop('诸葛王朗'))
print(score)
print(score.pop('郭靖', 60))
print(score)
# 清空字典
score.clear()
print(score)

















