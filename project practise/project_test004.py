'''
复制的玄学
'''
'''
Python 他在创造之初，就有这么个约定，
列表中直接存放的数值，字符，和存 class 实例，列表，字典不同。 对数值字符的复制，直接是复制的值，而不是一个投影。

'''
l = [1,2,3]
_l = l.copy()
_l[0] = -1
print(_l)
print(l)

'''
明明源列表是 mp3 的，怎么被复制后的列表改变成了 mp4 了，自动升了个级？查阅 Python 的说明书，你就会发现， 
原来在 Python 中复制东西，有两种方式，一种是深拷贝，一种是浅拷贝
'''

#copy() 源列表 l 去 _l
# 源列表值也被修改了
l = [[1,2,3],[2],3]
_l = l.copy()
_l[0][0] = -1
print(_l)
print(l)



class File:
    def __init__(self,name):
        self.name = name

audio = File("mp3")
file = File("txt")
l = [audio, file]
_l = l.copy()
_l[0].name = "mp4"
print(_l[0].name)
print(l[0].name)


'''
如果我想做对存放实例的列表做 Deep Copy 深拷贝的时候咋办
Python 自带了一个 copy 的库，里面就有一个 deepcopy，用这个你就能实现完全的深拷贝。
project005解了注释
'''
from copy import deepcopy
l = [[1,2,3],[2],3]
_l = deepcopy(l)
_l[0][0] = -1
print(l)
print(_l)


class File:
    def __init__(self,name):
        self.name = name

audio = File("mp3")
file = File("txt")
l = [audio, file]
_l = deepcopy(l)
_l[0].name = "mp4"
print(l[0].name)
print(_l[0].name)






