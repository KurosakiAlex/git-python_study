'''
在循环中运用的例子
'''

files = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]
for i in range(len(files)):
    if files[i] == "f3.txt":
        print("I got f3.txt")
        print(i)


files = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]
for f in files:
    if f == "f3.txt":
        print("I got f3.txt")
        print(f)


files = {"ID": 123, "passport": "china_passport", "books": [1,2,3]}
for key in files.keys():
    print("key:",key)

for value in files.values():
    print("value:",value)

for key,value in files.items():
    print("key:", key, "value:", value )




file = []
for i in range(5):
    file.append("f"+str(i)+".txt") #在最后添加一个元素
    print("has", file)

for i in range(len(file)):
    print("pop", file.pop())   #从最后一个pop出
    print("remain", file)




files = ["f1.txt", "f2.txt"]
# 扩充另一个列表
files.extend(["f3.txt", "f4.txt"])
print(files)
#按位置添加
files.insert(1,"f5.txt")
print(files)
#移除某索引
del files[4]
print(files)
#移除某个值
files.remove("f3.txt")
print(files)





files = {"ID01": 111, "passport": "my passport", "books": [1,2,3]}
# 按key拿取，并在拿取失败的时候给一个设定好的默认值
print('files["ID"]', files["ID01"])
print('files.get("ID"):',files.get("ID02", "NOT FOUND THIS ID"))
#将另一个字典补充到当前字典
files.update({"files":["01",1]})
print(files)
#pop调用一个item,和列表pop一样
popped = files.pop('books')
print('popped', popped)
print("remain", files)








