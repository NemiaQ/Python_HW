# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int
import random

my_list = []
n = int(input('Введите длину списка: '))

for i in range(n):
    my_list.append(input(f'Введите значение {i + 1}: '))
print(f'Исходный список: {my_list}')

for i in range(n):
    num = random.randint(0, n - 1)
    temp = my_list[i]
    my_list[i] = my_list[num]
    my_list[num] = temp
print(f'Новый список: {my_list}')
