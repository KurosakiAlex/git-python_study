'''
pickle/json 序列化
'''

import pickle
import os

data = {"filename:":" labfile", "creatime:":" today", "size:":1024}
pickle_data_str = pickle.dumps(data)
print(pickle_data_str)

with open("data.pkl", "wb") as f:
    pickle_data_file = pickle.dump(data, f)

print(os.listdir())

with open("data.pkl", "rb") as f:
    data = pickle.load(f)
print(data)




# 除了常见的字典，列表，元组这类的数据，pickle 甚至都可以打包 Python 的功能以及类
class File:
    def __init__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size

    def change_name(self, new_name):
        self.name = new_name


data = File("f2.txt", "now", 222)
# 存
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
# 读
with open("data.pkl", "rb") as f:
    read_data = pickle.load(f)
print(read_data.name)
print(read_data.size)






