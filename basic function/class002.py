# 上面两个类 Video Text 有共同属性,所以他们还可以抽象出一个更底层的类，就是“文件类”
# 我们可以通过继承的方式，将细分类嵌入到抽象类中，减少共有属性/功能的重复开发
class File:
    def __init__(self, name, create_time="today"):
        self.name = name
        self.create_time = create_time
        print("传进来了吗?", create_time)

    def get_info(self):
        return self.name + " is created at " + self.create_time




class Video(File):
    def __init__(self, name, windows_size=(1080, 720)):
        # self.name = name
        self.windows_size = windows_size
        # self.create_time = "today"
        a = "Tuesday"
        super().__init__(name=name, create_time=a)


class Text(File):
    def __init__(self, name, language="zh-cn"):
        # self.name = name
        self.language = language
        # self.create_time = "today"

        # 将共用属性的设置导入File父类
        super().__init__(name=name, create_time="next_day")

    # 在子类里复用父类功能
    def get_more_info(self):
        return self.get_info() + " using language of " + self.language



v = Video("my_video")
t = Text("my_text")

print(v.get_info())
print(t.create_time)
print(t.language)
print(t.get_more_info())



    


