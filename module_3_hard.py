# Задание "Раз, два, три, четыре, пять .... Это не всё?"

data_struct = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

list_instances = []
sum = 0


def calculate_sum_(params):
    summa = 0

    for i in range(len(data_struct)):
        # print(params[i], type(params[i]))

        if isinstance(params[i], list):
            # print(params[i])
            for j in range(len(params[i])):
                summa += int(params[i][j])

        elif isinstance(params[i], dict):
            print(params[i])
            for j in range(len(params[i])):
                pass

        elif isinstance(params[i], tuple):
            print(params[i])

        elif isinstance(params[i], str):
            # print(params[i])
            summa += len(params[i])

    print()
    return summa


def calculate_sum(params):
    summa = 0
    if isinstance(params, int):
        summa += params
    elif isinstance(params, str):
        summa += len(params)
    elif isinstance(params, (list, tuple, set)):
        for item in params:
            summa += calculate_sum(item)
    elif isinstance(params, dict):
        for key, value in params.items():
            summa += calculate_sum(key) + calculate_sum(value)
    return summa


# Main
print(f"Результат: {calculate_sum(data_struct)}")
#print(f"Результат: {calculate_sum_(data_struct)}")
