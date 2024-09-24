# "Файлы в операционной системе"

import os
import time

# Main
for root, dirs, files in os.walk('./'):
    print("Родительский католог:")
    print(root)
    print()

    print("Директории в родительском катологе:")
    for name in dirs:
        print(dirs)
        print()

    print("Файлфы в родительском катологе:")
    for name in files:
        #filepath = root + "/" + name
        filepath =os.path.join(root, name)
        filesize = os.path.getsize(filepath)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {name}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:'
              f'{formatted_time}, Родительская директория: {parent_dir}')

    print()


