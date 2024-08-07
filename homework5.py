immutable_var = (1, 2, "string", True)
print("Кортеж: ", immutable_var)
# immutable_var[0] = 5
# Traceback (most recent call last):
#   File "C:\Users\Yed\PycharmProjects\pythonProject\homework5.py", line 3, in <module>
#     immutable_var[0] = 5
#     ~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
print("")

mutable_list = [3, 4, "STRING", True]
print("Изначальный список: ", mutable_list)
mutable_list[0] = 5
mutable_list[1] = 6
mutable_list[2] = "string"
mutable_list[3] = False
print("Изменённый список: ", mutable_list)


# -= Result =-
#-----------------------------------------------------------------
# Кортеж:  (1, 2, 'string', True)
#
# Изначальный список:  [3, 4, 'STRING', True]
# Изменённый список:  [5, 6, 'string', False]
