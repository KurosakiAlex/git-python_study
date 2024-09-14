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


# 执行一次就会往后面写一行
with open("new_file.txt", "a+") as f:
    print(f.read())   #读不出来东西，因为光标在最后
    f.write("\nadd new line")
    f.seek(0)           # 将开始读的位置从写入的最后位置调到开头
    print(f.read())




