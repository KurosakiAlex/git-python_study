'''
字符串高级玩法

'''


#上面第二种，相对而言就算比较简单的，因为当字符串里面要传入的参数变多的时候， 第一种方式将会很混乱。
name = "莫烦Python"
print("我的名字是" + name + "！")
print("我的名字是%s!" % name)



name = "莫烦Python"
age = 18
gender = "男"
print("我的名字是" + name + "！我" + str(age) + "岁了，我是" + gender + "的~")
print("我的名字是 %s !我 %d 岁了，我是 %s 的~" % (name, age, gender))



#当你要在这句话中塞入更多参数时，即使是第二种也有可能不太适合了，因为我都不记得他们的顺序是怎样的，我很容易就填错了。
# 那么能不能用字典一样的模式来填入数据呢？
name = "莫烦Python"
age = 18
gender = "男"
print("我的名字是 %(nm)s !我 %(age)d 岁了，我是 %(gd)s 的~" % {"nm": name, "age":age, "gd":gender})



# 还有一个比较常用的方式，就是当你使用小数的时候，你会发现 %f 可以打印出很长一串数字。
# 有时候很占格子，我不喜欢，我可以让它短一点，输出固定长度的小数
print("%f" % (1/3))     # 后面不限制
print("%.2f" % (1/3))   # 后面限制 2 个位置
print("%4d" % (1/3))    # 前面补全最大 4 个位置
print("%5d" % 12)       # 前面补全最大 5 个位置



# format 更像是一个编辑字符串的功能，而非像百分号那样的固定搭配
name = "莫烦Python"
age = 18
height = 1.8
print("我的名字是 %s !我 %d 岁了，我 %f 米高~" % (name, age, height))
print("我的名字是 {} !我 {} 岁了，我 {} 米高~".format(name, age, height))



#我给 {} 里放一个数字，表示后面 format 里面的 index
name = "莫烦Python"
age = 18
height = 1.8
print("我的名字是 {0} !我 {1} 岁了，我 {2} 米高~我是{0}".format(name, age, height))


name = "莫烦Python"
age = 18
height = 1.8
print("我的名字是 {nm} !我 {age} 岁了，我 {ht} 米高~我是{nm}".format(nm=name, age=age, ht=height))


print("你 {:.3f} 米高".format(1.12345))
print("你 {ht:.1f} 米高".format(ht=1.12345))
print("你 {:3d} 米高".format(1))
print("你 {:3d} 米高".format(21))


'''
:,	每 3 个 0 就用逗号隔开，比如 1,000
:b	该数字的二进制
:d	整数型
:f	小数模式
:%	百分比模式
'''
txt = "You scored {:%}"
print(txt.format(2.1234))

txt = "You scored {:.2%}"
print(txt.format(2.1234))



# Python 3.6 之后引入的一个功能
# 使用 f 模式的情况下，我们要在字符串开头加上一个 f。然后用 {} 圈出你的变量名，直接在 {} 引用变量
name = "莫烦Python"
age = 18
height = 1.8
print(f"我的名字是 {name} !我 {age} 岁了，我 {height} 米高~")
# 甚至你还可以在 {} 里做运算
print(f"我 {age} 岁了，明年我就{age + 1}岁了~")



score = 2.1234
print(f"You scored {score:.2%}")
print(f"You scored {score:.3f}")
print(f"You scored {12:5d}")



print("你|帮|我|拆分|一下|这句话".split("|"))
print("|".join(["你","帮", "我", "重组", "一下", "这句话"]))



print("我在街头看到你".startswith("我在"))
print("我在街头看到你".startswith("街头"))
print("我在巷尾看到你".endswith("看到你"))
print("我在巷尾看到你".endswith("巷尾"))




















