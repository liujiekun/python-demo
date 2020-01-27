import matplotlib.pyplot as plt
x_values = list(range(0, 5))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues,edgecolor='none', s=40)
# 设置图表标题并给坐标轴加上标签
plt.show()
