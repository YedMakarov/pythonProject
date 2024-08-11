# Задание "Слишком древний шифр"
def create_pairs(num):
#    pass
    while num <= num:
        pass
    return num


first_list = []
second_list = []

num = int(input("Введите число в диапазоне 3 - 20 :"))
if num >= 3 and num <= 20:
    pass
else: print("Вы ввели неправильное число")

for i in range(num):
    i += 1
    for j in range(1, num):
        if i != j:
            if num % (i + j) == 0:
                first_list.append(i)
                second_list.append(j)

print(first_list)
print(second_list)


