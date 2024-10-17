# Задача "За честь и отвагу!"
from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")

        count_power = 100
        count_day = 0

        for i in range(int(count_power / self.power)):
            if count_power != 0:
                count_power -= self.power
                count_day += 1
                print(f"{self.name}, сражается {count_day} день(дня)..., осталось {count_power} воинов.")
                sleep(1)

        print(f"{self.name} одержал победу спустя {count_day} дней(дня)!")


# Main

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
