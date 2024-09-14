
with open("covid19_day_wise.csv", "r", encoding="utf-8") as f:
    data = f.readlines()

covid = {
    "date": [],
    "data": [],
    "header": [h for h in data[0].strip().split(",")[1:]]
}
for row in data[1:]:
    split_row = row.strip().split(",")
    covid["date"].append(split_row[0])
    covid["data"].append([float(n) for n in split_row[1:]])
print(covid)

print("日期列表摘取：", covid["date"][:4])


# 获取 2020 年 2 月 3 日的所有数据
date_idx = covid["date"].index("2020-02-03")
print("日期-->索引转换", date_idx)
import numpy as np
data = np.array(covid["data"])
print(data)
# zip() 函数会逐个从这两个可迭代对象中取出元素进行配对，然后返回一个迭代器，每次迭代都会产生一个元组，其中包含了对应位置上的两个元素。
# 如果其中一个可迭代对象比另一个短，那么 zip() 函数会在较短的对象用完后停止迭代。
for header, number in zip(covid["header"], data[date_idx]):
    print(header, ":", number)


# 2020 年 1 月 24 日之前的累积确诊病例有多少个？
row_idx = covid["date"].index("2020-01-24")     # 获取日期索引
column_idx = covid["header"].index("Confirmed") # 获取标题的索引
confirmed0124 = data[row_idx, column_idx]
print("截止 1 月 24 日的累积确诊数：", confirmed0124)


# 2020 年 7 月 23 日的新增死亡数是多少？
row_idx = covid["date"].index("2020-07-23")   # 获取日期索引
column_idx = covid["header"].index("New deaths")   # 获取标题的索引
result = data[row_idx, column_idx]
print("截止 7 月 23 日的新增死亡数：", result)


# 从 1 月 25 日到 7 月 22 日，一共增长了多少确诊病例？
row1_idx = covid["date"].index("2020-01-25")
row2_idx = covid["date"].index("2020-07-22")
new_cases_idx = covid["header"].index("New cases")
# 注意要 row1_idx+1 得到从 01-25 这一天的新增
# row2_idx+1 来包含 7 月 22 的结果
new_cases = data[row1_idx+1: row2_idx+1, new_cases_idx]
print(new_cases)
overall = new_cases.sum()
print("共新增：", overall)



# 画图展示新增确诊的变化曲线
import matplotlib.pyplot as plt
import threading
def plot_newcase_thread():
    new_cases_idx = covid["header"].index("New cases")
    plot_newcases_data = data[:, new_cases_idx]
    plt.plot(plot_newcases_data)
    plt.savefig('new_cases_plot.png')  # 保存图形为文件
    plt.close()  # 关闭图形绘制

    # plt.show(block=False)  # 显示图形，不阻塞后续代码
    # plt.pause(5)  # 等待5秒钟
    # plt.close()  # 关闭图形窗口
def plot_deathratio():
    death_ratio_idx = covid["header"].index("Deaths / 100 Cases")
    plot_deathratio_data = data[:, death_ratio_idx]
    plt.plot(plot_deathratio_data)
    plt.savefig('death_ratio_plot.png')  # 保存图形为文件
    plt.close()  # 关闭图形绘制
def print_date():
    print(covid["date"][50])


# # Matplotlib 要求在创建和管理图形时必须在主事件循环中执行。在某些情况下，当您尝试在非主线程中创建或显示 Matplotlib 图形时，会导致此错误。
# # Matplotlib 不支持在多线程中同时显示图形。这会导致一些不确定的行为，可能会出现图形无法正常显示的问题。
# # 创建并启动线程
# plot_newcases = threading.Thread(target=plot_newcase_thread)
# plot_newcases.start()
# # 等待图形绘制完成
# plot_newcases.join()

#matplotlib绘图必须在主进程中才不会出错，上面的办法也可以但是会出错
plot_newcase_thread()
plot_deathratio()

# 执行 print 函数
print_date()


