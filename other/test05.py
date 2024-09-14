'''判断一个数是不是回文数的函数'''
'''
判断一个数是否是回文数通常可以通过以下步骤：

将数字转换为字符串：将数字转换为字符串，便于进行字符操作。
比较正序和逆序：将字符串按照顺序和逆序进行比较，如果相等，则该数字是回文数。
'''

# def palindrome(num):
#     str_num = str(num)
#     if str_num == str_num[::-1]:
#         print('是回文数')
#     else:
#         print('不是回文数')
#
# num = int(input("请输入要判断的数字是不是回文数:"))
# palindrome(num)


def palindrome02(num):
    total = 0
    temp = num
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    if total == num:
        return True
    else:
        return False

# num = int(input('请输入要判断的数字是不是回文数:'))
#
# print(palindrome02(num))

