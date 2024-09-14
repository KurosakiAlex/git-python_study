'''
解二次方程
'''


import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # 没有实根
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root  # 有一个实根
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2  # 有两个实根

# 示例方程：x^2 - 3x + 2 = 0
a = 1
b = -3
c = 2
root1, root2 = solve_quadratic(a, b, c)
print("根1:", root1)
print("根2:", root2)



