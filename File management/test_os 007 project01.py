import os

os.makedirs("project01/Alex", exist_ok=True)
os.rename("project01/Alex", "project01/Alexpy")
print(os.listdir("project01"))



