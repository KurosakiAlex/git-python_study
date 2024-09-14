from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
'''

在 line, = ax.plot(x, np.sin(x)) 这行代码中，line 是一个变量名，它用于接收 ax.plot(x, np.sin(x)) 返回的曲线对象。

在 Python 中，逗号 , 可以用于元组的解构赋值，即将元组中的各个元素分配给对应的变量。
因此，line, = ax.plot(x, np.sin(x)) 表示将 ax.plot(x, np.sin(x)) 返回的曲线对象解构为一个元组，然后将元组中的第一个元素（即曲线对象）赋值给变量 line。

这种写法常用于只有一个元素的元组的解构赋值，可以简洁地获取函数返回的单个值。
'''
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/10.0))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig=fig,
                              func=animate,
                              frames=100,
                              init_func=init,
                              interval=20,
                              blit=False)

plt.show()








