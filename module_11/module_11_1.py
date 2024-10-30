

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


plt.style.use('_mpl-gallery')

# Make data
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()




##################################
# numpy
##################################
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
# # Чтение данных из CSV файла
# data = pd.read_csv('data.csv')
#
# # Вывод первых 5 строк
# print(data.head())
#
# # Группировка данных по столбцу и вычисление средней зарплаты
# average_salary = data.groupby('Age')['Salary'].mean()
# print(average_salary)
#
# # Фильтрация данных: сотрудники с зарплатой выше 70000
# high_salary_employees = data[data['Salary'] > 70000]
# print(high_salary_employees)


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