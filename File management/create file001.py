
# 创建文件并打开
f = open("new_file.txt","w")
# 往文件里写东西
f.write("some text...")
# 关闭文件
f.close()





# 解释open这个内置函数的大概调用的方法
class ClassFoo:

    def func(self):
        print("func in ClassFoo")


class ClassBar:

    def func(self):
        print("func in ClassBar")


def foo(category):
    if category == 1:
        return ClassFoo()
    return ClassBar()


g = foo(1)
g.func()





