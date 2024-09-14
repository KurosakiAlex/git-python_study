'''
pickle/json 序列化
'''

import pickle

class File:
    def __init__(self, name, create_time, size):
        self.name = name
        self.size = size
        self.create_time = create_time
        self.file = open(name, "w")

    # pickle 出去需要且能被 pickle 的信息
    def __getstate__(self):
        pickled = {"name": self.name, "create_time": self.create_time, "size": self.size}
        return pickled

    # unpickle 加载回来，重组 class
    def __setstate__(self, pickled_dict):
        self.__init__(
            pickled_dict["name"], pickled_dict["create_time"], pickled_dict["size"]
        )

data = File("f3.txt", "wb", 222)
#存
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
#读
with open("data.pkl", "rb") as f:
    read_data = pickle.load(f)

print(read_data.name)
print(read_data.size)

# TypeError: '_io.TextIOWrapper' object is not callable
print(read_data.file())




