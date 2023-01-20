# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
# оставила пару print'ов для удобства проверки

import random

playing_field = [i for i in range(1, 10)]


def start():
    n = random.randint(0, 1)
    match n:
        case 0:
            print('Первый ход делает компьютер. Вы играете за "O"')
        case 1:
            print('Ваш первый ход. Вы играете за "X"')
    return n


def print_field(playing_field):
    text = '|'
    for i in range(len(playing_field)):
        if not i % 3 == 0 or i == 0:
            text += (str(playing_field[i]) + '|')
            if i == len(playing_field) - 1:
                print(text)
        elif i % 3 == 0:
            print(text)
            print('-------')
            text = '|' + str(playing_field[i]) + '|'


def print_empty(playing_field):
    text = '|'
    for i in range(len(playing_field)):
        if not i % 3 == 0 or i == 0:
            if str(playing_field[i]).isdigit():
                text += ' |'
            else:
                text += (str(playing_field[i]) + '|')
            if i == len(playing_field) - 1:
                print(text)
        elif i % 3 == 0:
            print(text)
            print('-------')
            if str(playing_field[i]).isdigit():
                text = '| |'
            else:
                text = '|' + (str(playing_field[i]) + '|')


def check_win(playing_field):
    for i in range(len(playing_field)):
        if i % 3 == 0 and (playing_field[i] == playing_field[i + 1] == playing_field[i + 2]):
            return True
        if i < 3 and (playing_field[i] == playing_field[i + 3] == playing_field[i + 6]):
            return True
        if (i == 6 or i == 8) and (playing_field[i] == playing_field[len(playing_field) // 2] == playing_field[i % (len(playing_field) // 2)]):
            return True


def check_identically(new_list, val):
    if new_list.count(val) == 2:
        for item in new_list:
            if str(item).isdigit():
                return item


def next_bot(new_list, val):
    count = 0
    if new_list.count(val) == 1:
        for item in new_list:
            if str(item).isdigit():
                count += 1  # чтобы ходил в ту же строку/столбец, в который ходил ранее, но при условии, если одну из ячеек не занял соперник
                if count == 2:
                    return item


def check_go_bot(func, playing_field, val):
    for i in range(len(playing_field)):
        if i % 3 == 0:
            new_list = []
            new_list.append(playing_field[i])
            new_list.append(playing_field[i + 1])
            new_list.append(playing_field[i + 2])
            num = func(new_list, val)
            if not num == None:
                return num
                break

        if i < 3:
            new_list = []
            new_list.append(playing_field[i])
            new_list.append(playing_field[i + 3])
            new_list.append(playing_field[i + 6])
            num = func(new_list, val)
            if not num == None:
                return num
                break

        if (i == 6 or i == 8):
            new_list = []
            new_list.append(playing_field[i])
            new_list.append(playing_field[len(playing_field) // 2])
            new_list.append(playing_field[i % (len(playing_field) // 2)])
            num = func(new_list, val)
            if not num == None:
                return num
                break


def add_value(playing_field):
    key = start()
    if key == 0:
        val1, val2 = 'X', 'O'
    else:
        val1, val2 = 'O', 'X'
    count = 1
    print_field(playing_field)
    while count <= len(playing_field):
        flag = False
        match key:
            case 0:
                print()
                print('Ход компьютера:')
                num = check_go_bot(check_identically, playing_field, val1)  # проверяет возможность победить
                print(f'# номер ячейки на победу {num}')
                if num == None:
                    num = check_go_bot(check_identically, playing_field, val2)  # проверяет возможность проиграть
                    print(f'# номер ячейки на перехват {num}')
                if num == None:
                    num = check_go_bot(next_bot, playing_field, val1)  # ходит рядом со своим симловом, если он уже есть на поле
                    print(f'# номер ячейки на ход {num}')
                while not num in playing_field:
                    num = random.randint(1, 10)
                playing_field[num - 1] = val1
                print_empty(playing_field)
                if check_win(playing_field):
                    print('Вы проиграли')
                    flag = True
                    break
                count += 1
                key = 1
            case 1:
                print()
                while True:
                    try:
                        num = int(input('Ваш ход. Укажите номер ячейки: '))
                        if not num in playing_field:
                            raise Exception
                        break
                    except Exception:
                        print('Неверный номер ячейки! Укажите номер пустой ячейки.')
                        print_field(playing_field)
                playing_field[num - 1] = val2
                print_empty(playing_field)
                if check_win(playing_field):
                    print('Вы выиграли!')
                    flag = True
                    break
                count += 1
                key = 0
    if not flag:
        print()
        print('Ничья!')


add_value(playing_field)
