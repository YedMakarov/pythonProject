# Со списком ниже прекрасно справляется данный код
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

count = 0

while True:
    if my_list[count] > 0:
        print (my_list[count])
        count += 1
    elif my_list[count] == 0:
         count += 1
         continue # сугубо для применения continue
    else: break


print("") # Для разделения списков при выводе`


# С таким списком необходима проверка чтобы не выйти за границу списка
my_list = [42, 69, 0, 322, 13, 0, 99, 5, 9, 8, 7, 6, 5]

count = 0

while True:
    if my_list[count] > 0 and count < len(my_list) :
        print (my_list[count])
        count += 1
        if count == 13:
            break
    elif my_list[count] == 0:
            count += 1
            continue # сугубо для применения continue
    else: break
