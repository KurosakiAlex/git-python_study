'''判断一个数是不是素数的函数

基于平方根的试除法
由于一个数n的因子是成对出现的，
如a * b = n，其中a和b中至少有一个小于或等于√n，因此我们只需要检查2到√n之间的数即可。这显著减少了需要检查的次数，提高了效率
'''

def is_prime(num):
    factor = 0
    for factor in range(2, int(num ** 0.5)+1):
        if num % factor == 0:
            return False
    if num != 1:
        return True
    else:
        return False



# num = int(input("请输入素数:"))
# is_prime = is_prime(num)
#
# print(is_prime)






