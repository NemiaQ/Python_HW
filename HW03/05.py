# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib_pos(n):
    if n in [1, 2]:
        return 1
    elif n == 0:
        return 0
    else:
        return fib_pos(n - 1) + fib_pos(n - 2)


def fib_neg(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return fib_neg(n + 2) - fib_neg(n + 1)


my_list = []
num = int(input('Введите число: '))
for i in range(-num, num + 1):
    if i < 0:
        my_list.append(fib_neg(i))
    else:
        my_list.append(fib_pos(i))

print(my_list)
