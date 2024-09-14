
# with 语句是 Python 中用于管理资源的一种方式，它可以自动管理资源的分配和释放，无论代码块是否出现异常。
# 在这个例子中，with 语句用于打开文件，并在代码块结束时自动关闭文件。
with open("new_file2.txt", "w") as f:
    f.writelines(["some text for file2...\n", "2nd line\n"])



