'''
pickle/json 序列化
'''

import json

data = {"filename": "f1.txt", "create_time": "today", "size": 111}
j = json.dumps(data)
print(j)
print(type(j))



data = {"filename": "f1.txt", "create_time": "today", "size": 111}
with open("data.json", "w") as f:
    json.dump(data, f)

print("直接当纯文本读：")
with open("data.json", "r") as f:
    print(f.read())

print("用 json 加载了读：")
with open("data.json", "r") as f:
    new_data = json.load(f)
print("字典读取：", new_data["filename"])





# json打包 class 会报错的代码

class File:
    def __init__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size

    def change_name(self, new_name):
        self.name = new_name


data = File("f4.txt", "now", 222)
# 存，会报错
with open("data.json", "w") as f:
    json.dump(data, f)





