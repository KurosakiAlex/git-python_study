'''
raise手动触发异常

在使用的时候，可以查询Python异常错误名称表
'''

#raise 是你为别人犯错留下的证据，或者是告诉别人你怎么犯错的
# 你写了成百上千行代码，你也不能全记住代码的每一个细节。所以一旦报错，你也需要一个友善的错误信息提示
def no_negative(num):
    if num < 0:
        raise ValueError("I said no negative")
    return num


no_negative(-1)

# print(no_negative(-1))


