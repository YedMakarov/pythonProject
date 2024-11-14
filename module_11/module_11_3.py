# Задание по теме "Интроспекция"


import inspect


def introspection_info(obj):
    info = {}

    # Получаем тип объекта
    info['type'] = str(type(obj))

    # Получаем атрибуты объекта
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

    # Получаем методы объекта
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]

    # Получаем модуль, к которому принадлежит объект
    # info['module'] = obj.__module__
    if inspect.isclass(obj):
        info['module'] = obj.__module__

    # Другие интересные свойства объекта
    if isinstance(obj, (list, dict, set, tuple, str)):
        info['length'] = len(obj)

    if inspect.isclass(obj):
        info['is_class'] = True
    else:
        info['is_class'] = False

    # Возвращаем словарь с информацией
    return info


# Пример работы
number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("Hello")
print(string_info)

list_info = introspection_info([1, 2, 3])
print(list_info)


class Sample:
    def __init__(self):
        self.atribute_1 = 27

    def some_method(self):
        pass


class_info = introspection_info(Sample)
print(class_info)
