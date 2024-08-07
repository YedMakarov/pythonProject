
first = input("Введите первое число: ")
second = input("Введите второе число: ")
thrid = input("Введите третье число: ")

if first == second and second == thrid:
    print(3)
elif first == second:
    print (2)
elif second == thrid or first == thrid:
    print (2)
#elif first== thrid:
#    print (2)
else:
    print(0)

