import matplotlib.pyplot as plt
import numpy as np


x_coords = np.linspace(-100, 100, 1000)
y_coords = np.linspace(-100, 100, 1000)
points = []
for y in y_coords:
    for x in x_coords:
        if((x*0.03)**2+(y*0.03)**2-1)**3-(x*0.03)**2*(y*0.03)**3<=0:
            points.append({"x":x,"y":y})
heart_x = list(map(lambda point:point['x'],points))
heart_y = list(map(lambda point:point['y'],points))

plt.scatter(heart_x, heart_y,s=5,c=range(len(heart_x)),cmap="Reds")

plt.axis("off")
plt.show()




