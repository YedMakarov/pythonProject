import matplotlib.pyplot as plt

import numpy as np
from matplotlib import cm

import pandas as pd

##################################
# matplotlib
##################################
# Данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание линейного графика
plt.plot(x, y, marker='o')
plt.title("Пример линейного графика")
plt.xlabel("X-ось")
plt.ylabel("Y-ось")
plt.grid()
plt.show()

# Создание гистограммы
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, alpha=0.5, color='blue')
plt.title("Гистограмма")
plt.xlabel("Значения")
plt.ylabel("Частота")
plt.show()

# Создание поверхности
plt.style.use('_mpl-gallery')

# Make data
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

ax.set_title("Пример поверхностного графика")
ax.set_xlabel("X-ось")
ax.set_ylabel("Y-ось")
ax.set_zlabel("Z-ось")
# ax.set_zlim(0, 2)
# ax.set_zlim(-1, 1)


#############################
vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]

# plt.pie(vals, labels=labels)
plt.figure(figsize=(6, 6))
plt.pie(vals, labels=labels, autopct='%1.1f%%',
        colors=[
            # matplotlib named colors
            'tomato', 'cornflowerblue', 'gold', 'orchid', 'green',
        ]
        )
plt.title("Распределение марок автомобилей на дороге", fontdict={"fontsize": 14})
plt.show()

##################################
# numpy
##################################
print(f"\nВывод для работы с модулем - Numpy\n\
---------------------------------\n")

# Создание массива
array = np.array([1, 2, 3, 4, 5])

# Выполнение математических операций
mean_value = np.mean(array)
sum_value = np.sum(array)
std_dev = np.std(array)

print(f"Среднее: {mean_value}, Сумма: {sum_value}, Стандартное отклонение: {std_dev}")

# Создание двумерного массива и выполнение операции
matrix = np.array([[1, 2], [3, 4]])
transposed_matrix = np.transpose(matrix)
print(transposed_matrix)

##################################
# pandas
##################################
print(f"\nВывод для работы с модулем - Pandas\n\
-----------------------------------\n")

# Чтение данных из CSV файла
data = pd.read_csv('data.csv')

# Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(data.head())

# Анализ данных
average_age = data['Age'].mean()
average_salary = data['Salary'].mean()

print(f"\nСредний возраст: {average_age}")
print(f"Средняя зарплата: {average_salary}")

# Группировка данных по возрасту и подсчет средней зарплаты
salary_by_age = data.groupby('Age')['Salary'].mean()

print("\nСредняя зарплата по возрасту:")
print(salary_by_age)
