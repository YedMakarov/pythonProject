# Задание "Они все так похожи"


class Figure:
    filled = True

    def __init__(self, color, sides):
        self.__color = color
        self.__sides = sides

    def get_color(self):
        pass

    def set_color(self):
        pass

    def __is_valid_color(self):
        pass

    def get_sides(self):
        pass

    def set_side(self, *new_sides):
        pass

    def __is_valid_sides(self):
        pass

    def __len__(self):
        pass


class Circle(Figure):
    sides_count = 1
    pass
    # def __init__(self):
    #     super().__init__()
    #     __radius = self.sides / (2 * pi)

    def get_square(self):
        pass


class Triangle(Figure):
    sides_count = 3
    pass


class Cube(Figure):
    sides_count = 12
    pass


# Mfain

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
