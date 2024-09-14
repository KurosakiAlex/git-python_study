'''
class私有属性
'''

class File:
    def __init__(self):
        self.name = "f1"
        self.__delete = True
        self._type = "txt"

    def delete(self):
        self.__foce_delete()

    def __force_delete(self):
        self.__delete = True
        print("运行过了这里_force")
        return True

    def _soft_delete(self):
        self.__force_delete()
        print("运行过了这里_soft")
        return True

f = File()

# _ 一个下划线开头	弱隐藏 不想让别人用 （别人在必要情况下还是可以用的）
print(f._type)
print(f._soft_delete())

# __ 两个下划线开头	强隐藏 不让别人用
# print(f.__delete)
# print(f.__force_delete())











