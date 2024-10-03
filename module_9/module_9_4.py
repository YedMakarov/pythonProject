# Задача "Функциональное разнообразие".

# #######################################
# Lambda-функция
# first = 'Мама мыла раму'
# second = 'Рамена мало было'
#
# result = list(map(lambda x, y: True if x == y else False, first, second))
# print(result)


# #######################################
# # Замыкание
# def get_advanced_writer(file_name):
#     def write_everything(*data_set):
#         with open(file_name, "w", encoding='utf-8') as file:
#             for data in data_set:
#                 file.write(f"{data}\n")
#
#     return write_everything
#
#
# # Main - Замыкание
# write = get_advanced_writer('example.txt')
# write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# #######################################
# # Метод __call__
# from random import choice
#
#
# class MysticBall:

#     def __init__(self, n):
#       self.n = n
#
#     def __call__(self, x):
#       result = www
#       return result
#
# # Main - Метод __call__
# first_ball = MysticBall('Да', 'Нет', 'Наверное')
# print(first_ball())
# print(first_ball())
# print(first_ball())
