count = 0
l = [11,22,33,44]
for data in l:
    # print(data)
    if count == 2:
        data += 11
        print(data)
    l[count] = data
    count += 1
print(l)




name = ["a", "b", "c"]
score = [1,2,3]
d = {}
for i in range(3):
    d[name[i]] = score[i]
print(d)

name = ["a", "b", "c"]
score = [1,2,3]
d = {}
for n, s in zip(name, score):
    d[n]=s
print(d)


print("******************** reverse ***********************")
#reverse & reversed
l = [1, 2, 3]
_l = []
for i in range(len(l)):
    _l.append(l[-i-1])
print(_l)

#简化写法
l = [1,2,3]
_l = [l[-i-1] for i in range(len(l))]
print(_l)

l = [1,2,3]
l.reverse()
print(l)


# 切片操作的语法是 start:stop:step  而这里面start和stop都为空
l = [1,2,3]
_l = l[::-1]
print(l)
print(_l)

