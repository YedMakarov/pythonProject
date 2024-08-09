# Задача "Распаковка"

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)
    print(list_my)


values_list = [11, 'Строка', False]
values_list_2 = [54.32, 'Строка']

values_dict = {'a': 7, 'b': 8, 'c': 9}

# Main
# -1-
print_params()
print_params(4, 5, 6)
print_params(25, c=37)
print_params(b=25)
print_params(c=[1, 2, 3])
print("")  # Для разделения выводимых частей

# -2-
print_params(*values_list)
print_params(**values_dict)
print("")  # Для разделения выводимых частей

# -3-
print_params(*values_list_2, 42)
print("")  # Для разделения выводимых частей

# -4-
append_to_list(1)
append_to_list(3)
