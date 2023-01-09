# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов,
# отличной от 0.

import random
from decimal import Decimal as d

my_list = []

for _ in range(10):
    index = random.randint(0, 3)
    my_list.append(round(random.uniform(0, 10), index))

print(f'Список: {my_list}')

min = 1
max = 0

for i in my_list:
    if round(d(abs(i) - int(i)), 3) > max:
        max = round(d(abs(i) - int(i)), 3)
    if 0 < round(d(abs(i) - int(i)), 3) < min:
        min = round(d(abs(i) - int(i)), 3)

if min == 1 and max == 0:
    print('Все числа целые')
else:
    print(f'Разница между максимальным ({max}) и минимальным ({min}) значением дробной части: {max - min}')
