'''
try-except-else

try-except-finally
'''



print("***************try-except-else*****************")
# try-except-else 的模式，在 else 中处理没有报错的情况
l = [1,2,3,4]
try:
    l[3] = 4
except IndexError as e:
    print(e)
else:
    print("no error, now in else")





print("**************try-except-finally****************")
# try-except-finally
# 如果 else 是为了执行没有异常的状况，那么 finally 就是为了执行 不管有没有异常 的情况。
# 无论有报错还是没报错，finally 下面的代码都会运行
l = [1,2,3]
try:
    l[3] = 4
except IndexError as e:
    print(e)
finally:
    print("reach finally")



print("*****************try-finally********************")
# 有些时候，不管你有没有报错，你都想让程序去执行什么。我们甚至都不需要为任何异常做任何处理。
# 这种时候，也就是说，你有异常吧，我不让你终止主程序，你没有异常吧，万事大吉
try:
    dddd = dddddd
finally:
    print("I know there is error, so what?")

