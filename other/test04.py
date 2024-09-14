'''实现计算求最大公约数和最小公倍数的函数。'''

# 最大公约数
def calculate_gcd(x, y):
    if (x > y):
        (x, y) = (y, x)

    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

# 最小公倍数
def calculate_lcm(x, y):
    if(x > y):
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

x = int(input('x = '))
y = int(input('y = '))
gcd_result = calculate_gcd(x, y)
lcm_result = calculate_lcm(x, y)
print('最大公约数是:%d, 最小公倍数是:%d' % (gcd_result, lcm_result))




