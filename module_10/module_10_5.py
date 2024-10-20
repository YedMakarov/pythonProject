# Задача "Многопроцессное считывание".

import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            # all_data.append(line.strip())
            all_data.append(line)
    return all_data


def linear_read(files):
    start_time = datetime.datetime.now()
    for file in files:
        data = read_info(file)
    end_time = datetime.datetime.now()
    print(f"{end_time - start_time:} (линейный)")


def multiprocessing_read(files):
    start_time = datetime.datetime.now()
    with Pool() as pool:
    # with Pool(processes=4) as pool:
        results = pool.map(read_info, files)
    end_time = datetime.datetime.now()
    print(f"{end_time - start_time} (многопроцессный)")
    return results


# Main
if __name__ == "__main__":
    # Список файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    linear_read(filenames)

    # Многопроцессный вызов
    multiprocessing_read(filenames)
