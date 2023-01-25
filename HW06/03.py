# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_list = []
n = int(input('Введите длину списка: '))

for i in range(n):
    my_list.append(int(input(f'Введите значение {i + 1}: ')))

print(f'Исходный список: {my_list}')
# было:
# my_list2 = []
# for i in range((len(my_list) + 1) // 2):
#     my_list2.append(my_list[i] * my_list[len(my_list) - 1 - i])

my_list2 = [my_list[i] * my_list[len(my_list) - 1 - i] for i in range((len(my_list) + 1) // 2)]

print(f'Произведение пар чисел в списке: {my_list2}')
