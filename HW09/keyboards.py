from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_start = KeyboardButton('/start')
btn_help = KeyboardButton('/help')
btn_contact = KeyboardButton('/contact', request_contact=True)
btn_set = KeyboardButton('/set 200')
btn_location = KeyboardButton('/loc👀', request_location=True)

kb_main_menu.add(btn_start)
kb_main_menu.add(btn_help, btn_contact)
kb_main_menu.add(btn_set, btn_location)

kb_candies = ReplyKeyboardMarkup(resize_keyboard=True)

kb_candies.add(KeyboardButton(1), KeyboardButton(2), KeyboardButton(3), KeyboardButton(4), KeyboardButton(5))
kb_candies.add(KeyboardButton(6), KeyboardButton(7), KeyboardButton(8), KeyboardButton(9), KeyboardButton(10))
kb_candies.add(KeyboardButton(11), KeyboardButton(12), KeyboardButton(13), KeyboardButton(14), KeyboardButton(15))
kb_candies.add(KeyboardButton(16), KeyboardButton(17), KeyboardButton(18), KeyboardButton(19), KeyboardButton(20))
kb_candies.add(KeyboardButton(21), KeyboardButton(22), KeyboardButton(23), KeyboardButton(24), KeyboardButton(25))
kb_candies.add(KeyboardButton(26), KeyboardButton(27), KeyboardButton(28))
