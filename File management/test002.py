'''
w	（创建）写文本
r	读文本，文件不存在会报错
a	在文本最后添加
wb	写二进制 binary
rb	读二进制 binary
ab	添加二进制
w+	又可以读又可以（创建）写
r+	又可以读又可以写, 文件不存在会报错
a+	可读写，在文本最后添加
x	创建

'''


with open("new_file.txt", "r") as f:
    print(f.read())
with open("new_file.txt", "r+") as f:
    f.write("text has been replaced")
    f.seek(5)
#读取从第5个字节开始的12个字节内容，并打印
    print(f.read(12))

