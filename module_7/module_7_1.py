# Задача "Учёт товаров"

import os

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        # Создаем файл, если он не существует
        if not os.path.exists(self.__file_name):
            open(self.__file_name, 'w').close()

    def get_products(self):
        f = open(self.__file_name, 'r')
        f_str = f.read()
        f.close()
        return f_str

    def get_product_names(self):
        names = []
        products_data = self.get_products().strip().split('\n')
        for product_data in products_data:
            if product_data:
                name, weight, category = product_data.split(',')
                names.append(name.strip())
        return names

    def add(self, *products):
        # existing_products = set(self.get_products().split('\n'))
        existing_products = self.get_product_names()
        f = open(self.__file_name, 'a')

        for product in products:
            product_name = product.name
            if product_name in existing_products:
                print(f'Продукт {product_name} уже есть в магазине')
            else:
                f.write(f"{product}\n")

        f.close()


# Main
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
