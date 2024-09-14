import os.path

if os.path.exists("project01/Alex"):
    os.removedirs("project01/Alex")
    print("Alex removed")
else:
    print("Alex not exist")




