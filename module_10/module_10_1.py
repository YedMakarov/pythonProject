# Задача "Потоковая запись в файлы".

from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count: int, file_name: str):
    with open(file_name, "w", encoding='utf-8') as file:
        for i in range(word_count):
            data = (file.write(f"Какое-то слово № {i + 1} \n"))
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


# Main
# Линейный вариант
time_start = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
time_end = datetime.now()
print(time_end - time_start)

# Вариант с потоками
time_start = datetime.now()

thr_first = Thread(target=write_words, args=(10, "example5.txt"))
thr_second = Thread(target=write_words, args=(30, "example6.txt"))
thr_thrid = Thread(target=write_words, args=(200, "example7.txt"))
thr_four = Thread(target=write_words, args=(100, "example8.txt"))

thr_first.start()
thr_second.start()
thr_thrid.start()
thr_four.start()

thr_first.join()
thr_second.join()
thr_thrid.join()
thr_four.join()

time_end = datetime.now()
print(time_end - time_start)
