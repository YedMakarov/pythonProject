# Задание "Раз, два, три, четыре, пять .... Это не всё?"

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

list_instances = []
sum = 0


def calculate_structure_sum(params):
    global sum

    for i in range(len(data_structure)):
        # print(params[i], type(params[i]))

        if isinstance(params[i], list):
            # print(params[i])
            for j in range(len(params[i])):
                sum += int(params[i][j])

        elif isinstance(params[i], dict):
            print(params[i])
            for j in range(len(params[i])):
                pass

        elif isinstance(params[i], tuple):
            print(params[i])

        elif isinstance(params[i], str):
            # print(params[i])
            sum += len(params[i])

    print()
    return sum


# Main
print(f"Результат: {calculate_structure_sum(data_structure)}")
