import numpy as np
#
# cars = np.array([5, 10, 12, 6])
# print("数据：", cars, "\n维度：", cars.ndim)
#
# cars = np.array([
# [5, 10, 12, 6],
# [5.1, 8.2, 11, 6.3],
# [4.4, 9.1, 10, 6.6]
# ])
#
# print("数据：\n", cars, "\n维度：", cars.ndim)
#
# cars = np.array([
# [
#     [5, 10, 12, 6],
#     [5.1, 8.2, 11, 6.3],
#     [4.4, 9.1, 10, 6.6]
# ],
# [
#     [6, 11, 13, 7],
#     [6.1, 9.2, 12, 7.3],
#     [5.4, 10.1, 11, 7.6]
# ],
# ])
#
# print("总维度：", cars.ndim)
# print("场地 1 数据：\n", cars[0], "\n场地 1 维度：", cars[0].ndim)
# print("场地 2 数据：\n", cars[1], "\n场地 2 维度：", cars[1].ndim)
#
#

# cars1 = np.array([5, 10, 12, 6])
# cars2 = np.array([5.2, 4.2])
# cars = np.concatenate([cars1, cars2])
# print(cars)
#

test1 = np.array([5, 10, 12, 6])
test2 = np.array([5.1, 8.2, 11, 6.3])


# 首先需要把它们都变成二维，下面这两种方法都可以加维度
# 在轴 1 上添加新的长度为 1 的轴
test1 = np.expand_dims(test1, 1)
print(test1,"行列为：", test1.shape)
print("*********************************************")
'''
:：在第一个位置上使用 : 表示选取数组的所有行。
np.newaxis：np.newaxis 是 NumPy 中用于添加新轴的常量，它相当于 None。
在这里，np.newaxis 被用于在列轴（第二个轴）上添加一个新的长度为 1 的轴。
'''
test2 = test2[:, np.newaxis]
print(test2)
print(test2.shape)

# 然后再在第一个维度上叠加
all_tests = np.concatenate([test1, test2])
print("括展后\n", all_tests)







