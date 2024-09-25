# Задание "Программистам всё можно"

def add_everything_up(a, b):
    try:
        result = a + b
        return result

    except TypeError as exc:
        print(f'Встретились параметры разных типов - "{exc}", приводим их к типу "str".')
        return str(a) + str(b)


# Main

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
