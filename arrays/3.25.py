import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100, 101):
    x = x + [n]

# create y values
for n in x:
    y = y + [n * n - 3]

# draw chart
plt.plot(x, y)
plt.show()