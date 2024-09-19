# Задача "Записать и запомнить"

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, strings):
    open(file_name, 'w').close()

    strings_positions = {}

    file = open(file_name, 'a', encoding='utf-8')

    for i in range(len(info)):
        file_data = str(info[i])
        d_key = (int(f"{str(i + 1)}"), int(f"{file.tell()}"))
        d_value = f"{file_data}"
        strings_positions[d_key] = d_value
        file.write(f"{file_data}\n")
    file.close()

    return strings_positions


# Main
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
