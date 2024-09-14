def modify_name(file_name):
    file_name += "_file"
    file_name = "my_" + file_name
    print(file_name)

modify_name("test001")
modify_name("test002")





def myfunc(name, ext):
    filename = name
    total_name = filename + ext
    print(total_name)

myfunc("f3",".txt")






def modify_name(filename):
    filename += ".txt"
    filename = "my_" + filename
    return filename

new_filename = modify_name("f1")
print(new_filename)

print(modify_name("f2"))


def f(x, a=1,b=2, c=0):
    return a*x**2 + b*x + c/b

print(f(1))
print(f(1,2))

a = 2**2
print(a)




