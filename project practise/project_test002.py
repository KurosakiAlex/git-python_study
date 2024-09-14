'''
设计一个计算机
'''

import math

class Calculator:
    def subtract(self, a, b):
        return a - b
    def batch_subtract(self, a_list, b_list):
        res_list = []

        #这个地方曾出现过错误，需要注意
        #
        for i in range(len(a_list)):
            #self.subtract()是class内自己引用，自己用的
            res_list.append(self.subtract(a_list[i], b_list[i]))
        return res_list
c = Calculator()
print(c.subtract(2, 1))
print(c.batch_subtract([4,5,6], [1,2,3]))
a_ls = [7,8,9]
b_ls = [5,6,7]
print(c.batch_subtract(a_ls, b_ls))






