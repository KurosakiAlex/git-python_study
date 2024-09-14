# 从下面代码可以看出  调用模块功能的时候和调用Python类功能有异曲同工之处

# 调用module
import file as f1  #给模块重命名
print("f1:", f1.create_time())

# 调用class
class file:
    def create_time(self):
        return "new_file.txt"

f2 = file()

print("f2:", f2.create_time())

















