# Задача - Генераторные сборки".

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# first_result = (len(x)-len(y) for x )
second_result = (True if x == y else False for x in range(len(first)) for y in range(len(second)))

# Main
# print(list(first_result))
print(list(second_result))