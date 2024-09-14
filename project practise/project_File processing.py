'''
文件批量处理

替换所有文本中的特定片段
'''


import os
import re

#寻找文本
findfile = os.listdir("../File management/project01/Alex")
print(findfile)
#找到后拼接对应路径下的文件，并显示
for filename in findfile:
    #path = os.path.join(path1, path2, ..., pathN)
    # path1, path2, ..., pathN 是要拼接的路径片段
    #os.path.join() 函数会根据当前操作系统的规则，将这些路径片段拼接成一个完整的路径，并返回这个完整的路径。
    path_file = os.path.join("../File management/project01/Alex", filename)


    #下面这个with用来确认with会调用资源再释放的功能
    # with open(path_file, "r") as f:
    #     print(f.read())
    #     #第二次读不出来是因为有with会自动关闭调用的
    #     #使用 with 语句可以确保资源在使用完毕后正确释放，避免资源泄露和错误处理逻辑
    #     print(f.read())
    #     print(path_file, ":", f.read())


    # print(filename, type(filename))
    # print(path_file, type(path_file))
    #
    # #必须要open路径下的文件才行，不然只能打开当前文件夹下的文件。所以filename的文件打不开，只能打开path_file(所以需要拼接)
    # with open(path_file, "r") as f:
    #     res = re.findall(r'\w+ing', f.read())
    #     print(res)


    print("**************** replace ongoing....... *****************")


    #替换
    Document_file_path = "../File management/project01/Alex"
    with open(path_file,"r") as f:
        string = f.read()
        new_string = re.sub(r'(\w+)ing', 'doing', string)
        # print(new_string)
        with open(os.path.join(Document_file_path, "new_"+filename), "w") as f2:
            f2.write(new_string)
    with open(path_file, "r") as f:
        print(f.read())

    # if filename.startswith("new_"):
    #     continue
# with open(path_file, "r") as f:
#     print(path_file, ": ", f.read())







# string = "这是我的主页 https://mofanpy.com, 这个 www.mofanpy.com 有很多 mofan 教你机器学习和 python 语言的教学"
# res = re.findall(r'(https://)?(mofanpy.com)', string)
# for r in res:
#     print(r)
#     # print(r[0])




