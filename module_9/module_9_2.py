# Задача - "Списковые, словарные сборки".

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) > 4]
# second_result = [(x,y) if len(x) == len(y) else """""" for x in first_strings for y in second_strings]
second_result = [(x,y)  for x in first_strings for y in second_strings if len(x) == len(y)]
# third_result =


# Main

print(first_result)
print(second_result)
# print(third_result)

