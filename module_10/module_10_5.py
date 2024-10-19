# Задача "Многопроцессное считывание".

import datetime
import multiprocessing
# from multiprocessing import Pool

filenames = [f'./file {number}.txt' for number in range(1, 5)]
filenames_ = [f'./file_{number}.txt' for number in range(1, 5)]


def read_info(name):
    all_data = []

    for next_file in name:
        # print(next_file)
        # open(next_file, 'r').close()

        # Первый вариант
        current_file = open(next_file, 'r', encoding='utf-8')
        while True:
            line = current_file.readline()
            if not line:
                break
            all_data.append(line)
        current_file.close

        # Второй вариант
        # current_file = open(next_file, 'r')
        # lines = current_file.readlines()
        # for line in lines:
        #     all_data.append(line)
        # current_file.close

        # # Третий вариант
        # with open(next_file, 'r') as current_file:
        #     for line in current_file:
        #         all_data.append(line)
        # current_file.close


# Main

# # Линейный вызов
# start = datetime.datetime.now()
# # a = read_info(filenames)
# a = read_info(filenames_)
# stop = datetime.datetime.now()
# print(f"{stop - start} (линейный)")

# Многопроцессный
if __name__ == "__main__":
    start = datetime.datetime.now()
    # with multiprocessing.Pool() as pool:
    with multiprocessing.Pool(processes=2) as pool:
        a = pool.map(read_info, filenames_)
    stop = datetime.datetime.now()
    print(f"{stop - start} (многопроцессный)")
