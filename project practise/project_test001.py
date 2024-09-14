'''
设计一个计算机
'''
import math

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiplay(self, a, b):
        return a * b
    def devide(self, a, b):
        if b == 0:
            print("The denominater can not be zero")
        else:
            return a / b
    def nth_root(self, a, n):
        return a**(1/n)

    def solve_quadratic(self, a, b, c):
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return None  # 没有实根
        elif discriminant == 0:
            root = -b / (2 * a)
            return root, root  # 有一个实根
        else:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return root1, root2  # 有两个实根

#Create a instance
c = Calculator()
print(c.add(1, 2))
print(c.devide(6, 3))
print(c.multiplay(2, 3))
print(c.devide(2, 0))
print(c.nth_root(9, 3))

print(c.solve_quadratic(1, -3, 2))




