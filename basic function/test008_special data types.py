'''
数据种类
'''


print("*****************    list    抽屉   ************************")


# 列表    抽屉
files = ["f1.txt","f2.txt","f3.txt","f4.txt","f5.txt"]
print("files[:3]",files[:3])   #实际上的输出是第0个到第2个，实际上前面是闭括号，后面是开括号
print("files[2:4]",files[2:4])
print("files[-3:]",files[-3:])

#列表的数据还能随时替换
files[1] = 'a'
print(files)


#列表中，你可以存放不同类型的元素，字符，数字，甚至列表里还能有列表
z = [1,"file",["3",3.6]]
print(z)
z[2][0] = "被修改的列表值"
print(z)



print("*****************    Dict   贴了标签的抽屉   ************************")


#Dict字典    贴了标签的抽屉
files = {"ID" : 101, "passport" : "China passport", "books" : [4,5,6]}
print(files)
print(files["books"][1])


#通过 key 我们就能将对应的 value 进行修改
files["ID"] = 222
print(files)
files["ID"] = [3,2,1]
print(files)



print("*****************    Tuple   上了锁的抽屉   ************************")




#元组   上了锁的抽屉
lock_File = ("file01", "file02", "file03")
print(lock_File[1])
#lock_File[1] = "file05"  #如果想验证无法被修改，可以给这条解注释
#print(lock_File)   #上面修改的值是无法改变Tuple里的值的，会报错



print("*****************    Set   自动合并同类的抽屉   ************************")


#合集    自动合并同类的抽屉
# 常用在去重的时候,存储的无序的
# my_files = set(["file001", "file002", "file003"])
my_files = {"file001", "file002", "file003"}
print(my_files)

#去除重复项
my_files.add("file001")
print(my_files)

my_files.add("file005")
print(my_files)

my_files.remove("file002")
print(my_files)


# 交集并集的操作
print("my_files",my_files)

your_files = {"file001", "file002", "file003"}
print("your_file", your_files)

print("交集", your_files.intersection(my_files))
print("并集", your_files.union(my_files))
print("my_files补集", my_files.difference(your_files))
print("your_files补集",your_files.difference(my_files))
#补集：子集在全集中不同的一项









