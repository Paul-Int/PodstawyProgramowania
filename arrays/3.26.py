import matplotlib.pyplot as plt
import math

x = []
y = []

for angle in range(0, 361):
    x = x + [angle]
    radians = angle * math.pi / 180
    y = y + [math.sin(radians)]

plt.plot(x, y)
plt.show()