'''
Pythons生成器
现做现吃，省内存

'''


'''
这种需要先保存一个 items 的列表，但当你做机器学习或者数据处理的时候，
如果这个 items 列表的数据量很大，就会非常占内存。所以生成器的一个重要目的就是避免在内存中记录这样的一个大数据，避免把内存撑爆
'''
items = []  # 假设这里在记录一个很大的列表
for item in range(5):
    if item % 2 == 0:
        items.append(item)
for i in items:
    print(i)



# Generator   生成器
def need_return():
    for item in range(5):
        if item % 2 == 0:
            print("我要扔出去一个 item=%d 了" % item)
            yield item  # 这里就会返回给下面的 for 循环
            print("我又回到里面了")

for i in need_return():
    print("我在外面接到了一个 item=%d\n" % i)



# Generator   生成器
def need_return():
    tmp = 2
    for item in range(300):
        if item == tmp:
            tmp *= item
            yield item, tmp

for i in need_return():
    print(i)




def need_return(init_value):
    tmp = init_value
    for item in range(300):
        if item == tmp:
            tmp *= 2
            yield item

for i in need_return(10):
    print(i)




'''
定义生成器类
用一个 class 也是可以表示一个迭代器，生成器的。 如果我们将上面的逻辑转化成 class，这个 class 可能相对比较复杂，
但是也意味着你可以有更多设置和控制发生在这个 class 里面。里面我们申明了用于生成器的两个 method，__iter__ 和 __next__。

__iter__ 的意思是，当我在外面 for 循环进行迭代时，我返回什么？在下面例子中，我就把自己这个 class 本身返回回去，继续让自己做迭代就好了。

__next__ 的意思是每次迭代的时候，我的函数会放出来什么元素。下面的功能中实现的就是放出来一个被计算过的 item 元素。
'''
class NeedReturn:
    def __init__(self, init_value=0):
        self.tmp = init_value
        self.item = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.item == self.tmp:
                self.tmp *= 2
                return self.item
            self.item += 1
            if self.item == 300:
                raise StopIteration

for i in NeedReturn(5):
    print(i)






