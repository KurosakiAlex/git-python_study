'''
文件编码，中文乱码
'''

with open("chinese.txt", "wb") as f:
    f.write("这是中文， this is chinese".encode("gbk"))


with open("chinese.txt", "rb") as f:
    print(f.read())

# 先确认是哪一种文件编码，然后在读的时候，需要传入一个 encoding 的参数，表示用这一种编码来读。 这样中文乱码的问题就顺利解决了
with open("chinese.txt", "r", encoding="gbk") as f:
    print(f.read())






