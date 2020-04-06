import matplotlib.pyplot as plt

x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)


#  Заголовок диаграммы и меток осей
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

# Диапазон для каждой оси (x, y)
ax.axis([0, 1100, 0, 2100000])

plt.show()