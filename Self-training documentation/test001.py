

# 下面这个with用来确认with会调用资源再释放的功能


with open("path_file", "w") as f:
    f.write("Hello world !")
with open("path_file", "r") as f:
    print(f.read())

    #第二次读不出来是因为有with会自动关闭调用的
    #使用 with 语句可以确保资源在使用完毕后正确释放，避免资源泄露和错误处理逻辑
    print(f.read())

with open("path_file", "r") as f:
    print(f.read())

print(open("path_file", "r"))

f = open("path_file", "r")
print(f.read())

