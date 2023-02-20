from aiogram import types
from create import dp
import random
from keyboards import kb_main_menu
from keyboards import kb_candies

from asyncio import sleep
from datetime import datetime

count = 150
temp = 0


def game():
    global count
    global temp

    y = count % 29
    if y == 0:
        y = random.randint(0, 28)

    count -= y
    temp = y


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    global count
    new_count = 150
    count = new_count
    await message.answer(
        f'Привет, {message.from_user.first_name}. Мы будем играть в 🍭🍭🍭. За один ход можно взять не более 28 конфет. '
        f'\nВыиграет тот, кто заберет последнюю конфету. \nОбщее количество конфет {count}. '
        f'\nКоличество конфет можно изменить через команду "/set". \nМеню "/menu"')

    x = random.randint(0, 1)
    match x:
        case 0:
            await message.answer('Я хожу первым.')
            game()
            await message.answer(
                f'Я взял {temp} конфет(у). На столе осталось {count} конфет(а). Сколько возьмете Вы?',
                reply_markup=kb_candies)
        case 1:
            await message.answer('Ваш первый ход. Сколько конфет вы возьмете?', reply_markup=kb_candies)
    # await sleep(10)

    user = []
    user.append(datetime.today().strftime('%d.%m.%Y'))
    user.append(message.from_user.full_name)
    user.append(message.from_user.id)
    user.append(message.from_user.username)
    user = list(map(str, user))
    with open('text.txt', 'a', encoding='UTF-8') as data:
        data.write('\n')
        data.write(' | '.join(user))


@dp.message_handler(commands=['menu'])
async def mes_menu(message: types.Message):
    await message.answer('Выбери кнопку', reply_markup=kb_main_menu)


@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Никто не поможет.', reply_markup=kb_main_menu)


@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global count
    new_count = int(message.text.split()[1])
    count = new_count
    await message.answer(f'Общее количество конфет: {count}')


@dp.message_handler(content_types='location')
async def mes_loc(message: types.Message):
    print(message)
    await message.answer(f'Ха! Я знаю, где ты живешь 😈')


@dp.message_handler()
async def mes_all(message: types.Message):
    global count
    global temp

    if count > 0:
        if message.text.isdigit() and int(message.text) <= count and 0 < int(message.text) < 29:
            count -= int(message.text)
            if count == 0:
                await message.answer('Конфет не осталось! Поздравляю! Вы победили!')
                with open('text.txt', 'a', encoding='UTF-8') as data:
                    data.write(' | win\n')
            else:
                game()
                if count == 0:
                    await message.answer(
                        f'Я взял {temp} конфет(у). Конфет не осталось, {message.from_user.full_name}, Вы проиграли. Попробуйте еще раз!')
                    with open('text.txt', 'a', encoding='UTF-8') as data:
                        data.write(' | loss\n')
                else:
                    await message.answer(f'Я возьму...')
                    await sleep(1)
                    await message.answer(
                        f'{temp} конфет(у). На столе осталось {count} конфет(а). '
                        f'\nСколько возьмете Вы?', reply_markup=kb_candies)

        else:
            await message.answer(
                f'{message.from_user.full_name}, смотри, что я поймал: {message.text}. Жду цифру от 1 до 28 и не больше {count}')

    else:
        await message.answer(f'Игра закончена, конфет нет. Для новой игры введи команту "/start"',
                             reply_markup=kb_main_menu)
