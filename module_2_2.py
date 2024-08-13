# Условная конструкция. Операторы if, elif, else.
# Задача "Все ли равны?"
first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second and first == third and second == third:
    print(3) # если все числа равны между собой, то вывести 3
elif first == second or first == third or second == third:
    print(2) # если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
else:
    print(0) # если равных чисел среди 3-х вообще нет, то вывести 0