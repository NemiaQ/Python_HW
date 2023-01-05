# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
num = input('Введите чило: ')
sum_num = 0
for i in num:
    if i.isdigit():
        sum_num += int(i)
print(sum_num)
