'''
class
'''


class File:
    def __init__(self, name, create_time="today"):
        self.name = name
        self.create_time = create_time
    def change_name(self, new_name):
        self.new_name01 = new_name

    def get_info(self):
        return self.name + " is created at " + self.create_time

my_file = File("my_file")

print(my_file.name)
print(my_file.create_time)

#调用实例中类的功能
my_file.change_name("new_name")
print(my_file.new_name01)


print(my_file.get_info())


















