'''
pickle/json 序列化
'''

import pickle
import os

class File:
    def __int__(self, name, creat_time, size):
        self.name = name
        self.creat_time = creat_time
        self.file = open(name, "w")

data = File("f3.txt", "now", 222)

# pickle 存，会报错
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)




