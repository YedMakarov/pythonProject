# Задача "Потоки гостей в кафе".

from threading import Thread

class Table:
    def __init__(self, number: int):
        self.table = number
        self.guest = None


class Guest:
    def __init__(self, *name):
        pass



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
