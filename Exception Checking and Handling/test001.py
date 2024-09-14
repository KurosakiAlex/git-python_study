'''

"try-except" 是 Python 中用于异常处理的一种机制，它的语法是通过 try 和 except 关键字来实现。
'''

#解注释下面两段代码会有ERROR
# FileNotFoundError: [Errno 2] No such file or directory: 'no_file.txt'
# with open("no_file.txt", "r") as f:
#     print(f.read())

'''
try:
    # 可能会出现异常的代码块
    # 这里放置可能会抛出异常的代码
except ExceptionType:
    # 异常处理代码块
    # 这里放置捕获到异常时需要执行的代码
'''

try:
    with open("no_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print(e)
    with open("no_file.txt", "w") as f:
        f.write(" I'm no_file.txt")
    print("new file 'no_file.txt' has been written")










