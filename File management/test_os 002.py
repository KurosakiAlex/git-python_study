import os

# exist_ok 为确认要创建的dir存不存在，默认exist_ok=False
os.makedirs("project01", exist_ok=True) #已经有了要创建的dir，再exist_ok=True，就不会出错
print(os.path.exists("project01"))














