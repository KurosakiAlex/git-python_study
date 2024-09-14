# os.path.join() 函数处理了操作系统之间路径分隔符的差异（类 Unix 系统使用 /，Windows 使用 \），使您的代码更具可移植性
# 可以重组要连接在一起的路径的各个组件的字符串


import os
import shutil

def copy(path):
    dir_name, filename = os.path.split(path)
    # filename = os.path.basename(path)   #文件名
    # dir_name = os.path.dirname(path)    #文件夹名
    new_filename = "new_" + filename    #新文件名
    new_path = os.path.join(dir_name,new_filename)   #目录重组

    # shutil.copy2("source.txt", "destination.txt")
    # 这会将文件"source.txt"复制到"destination.txt"，并尽可能地保留"source.txt"的所有元数据。
    print(new_path)
    shutil.copy2(path, new_path) #复制文件
    print(new_path)

    return os.path.isfile(new_path), new_path

copied, new_path = copy("project01/Alex/a.txt")
if copied:
    print("copied to:", new_path)
else:
    print("copy failed")








