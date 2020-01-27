import matplotlib.pyplot as plt
squres = [2, 2, 3, 4, 5]
squres_power2 = []
for item in squres:
  squres_power2.append(item*item)
plt.plot(squres, squres_power2, lineWidth=5)
plt.scatter(squres, squres_power2, s=200)
plt.show()
