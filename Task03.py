# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint
my_list = []
for i in range(1, 11):
    my_list.append(i)
print()
print(f'Исходный список: {my_list}')

temp = my_list[0]
my_list_length = len(my_list)
for i in range(my_list_length):
    temp = my_list[i]
    random_position = randint(0, my_list_length-1)
    my_list[i] = my_list[random_position]
    my_list[random_position] = temp
    
print()
print(f'Перемешанный список: {my_list}')
print()