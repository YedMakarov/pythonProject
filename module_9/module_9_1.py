# Задача "Вызов разом"


def apply_all_func(int_list, *functions):
    result = {}

    for function_n in functions:
        result[function_n.__name__] = function_n(int_list)
    return result



# Main
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
