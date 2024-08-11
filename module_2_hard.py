# Задание "Слишком древний шифр"

str_result = ""

num = int(input("Введите число в диапазоне 3 - 20 :"))
if num >= 3 and num <= 20:
    pass
else: print("Вы ввели неправильное число")

for i in range(num):
    i += 1
    for j in range(1, num):
        if i != j:
            if num % (i + j) == 0:
                if i < j:
                    str_result += str(i) + str(j)

print(str_result)



