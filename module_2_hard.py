# Задание "Слишком древний шифр"


num = int(input("Введите число в диапазоне 3 - 20 :"))
if num >= 3 and num <= 20:
    pass

for i in range(num):
    i += 1
    for j in range(1, num):
        if i != j:
            if num % (i + j) == 0:

