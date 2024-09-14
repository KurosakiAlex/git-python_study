'''
全局变量和局部变量
'''



#局部变量和全局变量互相实现，各不影响

#但是有办法修改
#局部变量修改全局变量的例子
filename = "f1.txt"
def modify_name():
    global filename  # 提出申请
    filename = "f2.txt"
    print("local filename:", filename)
modify_name()
print("global filename:", filename)











