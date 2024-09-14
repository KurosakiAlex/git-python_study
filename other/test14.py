'''在屏幕上显示跑马灯文字。'''
'''os 是 Python 的标准库模块之一，用于与操作系统进行交互。
它提供了大量的函数来处理文件和目录'''
'''time 是 Python 的标准库模块之一，用于处理时间相关的任务。
它提供了各种函数来操作时间和日期。'''
import os
import time


current_directory = os.getcwd()
print("当前工作目录:", current_directory)

current_timestamp = time.time()
print("当前时间戳:", current_timestamp)
local_time = time.localtime(current_timestamp)
print("本地时间元组:", local_time)


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
# 清理屏幕上的输出
        os.system('cls') #windows清屏指令  os.system('clear') linux清屏指令
        print(content)
# 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()












