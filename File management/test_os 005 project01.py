import os

os.makedirs("project01/Alex", exist_ok=True)
with open("project01/Alex/a.txt", "w") as f:
    f.write("nothing......")
os.removedirs("project01/Alex")   #报错：OSError: [WinError 145] 目录不是空的。: 'project01/Alex'







