from aiogram import types
from create import dp
import random
from aiogram.dispatcher.filters import Text

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
        f'Привет, {message.from_user.first_name}. Мы будем играть в конфеты. За один ход можно взять не более 28 конфет. \nКонфеты достаются тому, кто заберет последнюю конфету. \nОбщее количество конфет {count}. \nКоличество конфет можно изменить через команду "/set"')
    await message.answer('Сколько конфет вы возьмете?')


@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global count
    new_count = int(message.text.split()[1])
    count = new_count
    await message.answer(f'Общее количество конфет: {count}')


@dp.message_handler()
async def mes_all(message: types.Message):
    global count
    global temp

    if count > 0:
        if message.text.isdigit() and int(message.text) <= count and 0 < int(message.text) < 29:
            count -= int(message.text)
            if count == 0:
                await message.answer('Конфет не осталось! Поздравляю! Вы победили!')
            else:
                game()
                if count == 0:
                    await message.answer(
                        f'Я взял {temp} конфет(у). Конфет не осталось, {message.from_user.full_name}, Вы проиграли. Попробуйте еще раз!')
                else:
                    await message.answer(
                        f'Я взял {temp} конфет(у). На столе осталось {count} конфет(а). Сколько возьмете Вы?')
        else:
            await message.answer(
                f'{message.from_user.full_name}, смотри, что я поймал: {message.text}. Жду цифру от 1 до 28 и не больше {count}')

    else:
        await message.answer(f'Игра закончена, конфет нет. Для новой игры введи команту "/start"')
