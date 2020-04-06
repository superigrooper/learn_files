import matplotlib.pyplot as plt

# Выбор силя оформления
plt.style.use('seaborn')

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fig, ax= plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#  Заголовок диаграммы и меток осей
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square value", fontsize=14)

# Размер шрифиа делений на осях
ax.tick_params(axis='both', labelsize=14)

plt.show()