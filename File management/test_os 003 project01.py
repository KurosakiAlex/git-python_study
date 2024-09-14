import os.path

if os.path.exists("project01/Alex"):
    print("pro/Alex already exist")
else:
    os.makedirs("project01/Alex")
    print("pro/Alex created")
print(os.listdir("project01"))



