# Задание "Программистам всё можно"

def add_everything_up(a, b):
    try:
        return a + b

    except TypeError as exec:
        return str(a) + str(b)


# Main

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
