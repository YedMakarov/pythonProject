# Задача "История строительства"

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)
                i += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # Сравнение
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    # Сложение
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __iadd__(self, value):
        # if isinstance(value, int):
        #     self.number_of_floors = self.number_of_floors + value
        #     return self
        return self.__add__(value)

    def __radd__(self, value):
        # if isinstance(value, int):
        #     self.number_of_floors = self.number_of_floors + value
        #     return self
        return self.__add__(value)

    def __del__(self):
        print(f"{self} снесён, но он останется в истории")
        return f"{self} снесён, но он останется в истории"


# Main
h1 = House('ЖК Эльбрус', 10)
#print(House.houses_history)
h2 = House('ЖК Акация', 20)
#print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
#print(House.houses_history)

# Удаление объектов
del h2
del h3

#print(House.houses_history)
