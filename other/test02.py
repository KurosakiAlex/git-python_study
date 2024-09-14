from random import randint
'''摇色子'''
def roll_dice(n):
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total
n = int(input("n = "))

print(roll_dice(n))



