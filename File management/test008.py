'''
文件目录多种检验
'''

import os
os.makedirs("project01/Alex", exist_ok=True)
with open("project01/Alex/a.txt", "w") as f:
    f.write("nothing......")
print(os.path.isfile("project01/Alex/a.txt"))  #True
print(os.path.exists("project01/Alex/a.txt"))  #True
print(os.path.isdir("project01/Alex/a.txt"))   #False
print(os.path.isdir("project01/Alex"))  #True











