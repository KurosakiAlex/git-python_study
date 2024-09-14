# 如何实现一个生成斐波拉切数列的生成器
def fib(quantity, max_num):
    a, b = 0, 1
    for _ in range(quantity):
        a, b = b, a + b
        if max_num > a:
            yield a
        else:
            break

def main(quantity, max_num):
    for val in fib(quantity, max_num):
        print(val)

if __name__ == '__main__':
    main(20, 80)








