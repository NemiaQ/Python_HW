# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
import random
import tkinter as tk

print('Приветствую! \nПравила игры: каждый игрок поочередно берет конфеты. '
      '\nЗа один ход можно взять не более 28 конфет. \nКонфеты достаются тому, кто заберет последнюю конфету. '
      '\nПриятной игры!')
count = int(input('Укажите количество конфет: '))
all_sweets = count


def start():
    x = random.randint(0, 1)
    match x:
        case 0:
            print('Первый ход делает компьютер.')
        case 1:
            print('Ваш первый ход.')
    return x


def game(count):
    x = start()
    while count > 0:
        match x:
            case 0:
                if count == all_sweets:
                    y = 0
                    while y == count % 29:
                        y = random.randint(0, 28)       # если комп стартует первым, дадим шанс игроку перехватить инициативу
                else:
                    y = count % 29
                if y == 0:
                    y = random.randint(0, 28)
                count -= y
                print(f'Компьютер взял {y} конфет(у).')
                if count == 0:
                    print('Конфет не осталось, Вы проиграли. Попробуйте еще раз!')
                x = 1
            case 1:
                print(f'На столе осталось {count} конфет(а)')
                while True:
                    try:
                        y = int(input('Сколько конфет вы возьмете? '))
                        if y > count or (not 0 < y < 29):
                            print('Неверное количество конфет!')
                            raise Exception
                        break
                    except Exception:
                        if count < 28:
                            print(f'Укажите количество конфет от 1 до 28 и не более {count}')
                        else:
                            print('Укажите количество конфет от 1 до 28')
                count -= y
                if count == 0:
                    print('Конфет не осталось! Поздравляем! Вы победили!')
                x = 0


game(count)