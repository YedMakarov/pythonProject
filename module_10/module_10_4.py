# Задача "Потоки гостей в кафе".

import random
import time
import threading
from queue import Queue


class Table:
    def __init__(self, number: int):
        self.table = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # Гость "ест" от 3 до 10 секунд
        eating_time = random.randint(3, 10)
        time.sleep(eating_time)


class Cafe:

    def __init__(self, tables):
        pass

    def guest_arrival(self):
        pass

    def discuss_guests(self):
        pass


# Main

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
