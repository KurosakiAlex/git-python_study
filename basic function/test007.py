'''
循环

'''


for i in range(3,10,2):
    print("新文件->" + str(i))



guess_num = 10
while guess_num != 20:
    guess_num += 1
    print(guess_num)


print('1***********************************')


count = 0
guess_num = 30
while guess_num != 10 and count <= 10:  #不满足and条件则跳出循环
    guess_num -= 1
    count += 1
    print(guess_num)


print('2***********************************')


count = 0
guess_num = 10
while guess_num != 9:
    guess_num += 1
    count += 1
    if count > 10:
        break      #if条件满足，则跳出循环
    print(guess_num)


print('3***********************************')


for i in range(10):
    if i % 2 == 0:
        continue  #跳过本次循环,进行下一圈循环
    print(i)




