d = {"name": "f1", "age": 2}
l = [1,2,3]
try:
    v = d["gender"]
    l[3] = 4
except (KeyError, IndexError) as e:
    print("key or index error for:", e)





print("********************************")


# 它不会同时处理字典的 KeyError 和列表的 IndexError，因为在程序顺序执行的时候，只要是报错了，
# 那么就会终止错误之后的代码，进入错误 回收 环节。这个回收环节在上面的案例中也就是 except 的错误处理环节。
# 所以你就能发现，其实在你不改动上面代码的情况下，l 列表是没有 append(4) 的。只有当字典正常的时候，列表的报错才会触发
d = {"name":"f1", "age":2}
l = [1,2,3]
try:

# 下面两条前后换下顺序可以交换
    v = d["gender"]
    l[3] = 4

except (KeyError) as e:
    print("key error for:", e)
    d["gender"] = "male"

except (IndexError) as e:
    print("index error for:", e)
    l.append(4)

print("added d:", d)
print("added l:", l)


