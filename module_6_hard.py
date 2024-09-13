# Задание "Они все так похожи"


class Figure:
    def __init__(self, sides, color, filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled

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
    pass


class Triangle(Figure):
    pass


class Cube(Figure):
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
