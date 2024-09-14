from test05 import palindrome02
from test06 import is_prime
if __name__ == '__main__':
    num = int(input('请输入一个数,判断其是否是回文素数:'))
    if palindrome02(num) and is_prime(num):
        print("%d是回文素数" % num)
    else:
        print("%d不是回文素数" % num)


