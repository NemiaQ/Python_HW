# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
from decimal import Decimal

n = int(input('Введите число: '))
nums = []
sum_nums = 0
for i in range(1, n + 1):
    number = round(((1 + 1 / i) ** i), 2)
    nums.append(number)
    sum_nums += number
print(f'Для n = {n}: {nums}')
print(f'Сумма: {sum_nums}')
