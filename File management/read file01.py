


f = open("new_file2.txt", "r")
print(f.read())
f.close()



with open("new_file2.txt", "r") as f:
    print(f.readlines())



with open("new_file2.txt","r") as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
        #如果一个字符串为空字符串 '' 或者一个空的可迭代对象（如列表、元组、字典等），它会被视为 False
            break









