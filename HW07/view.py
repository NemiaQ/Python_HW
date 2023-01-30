def main_menu() -> int:
    print()
    print('Главное меню:')
    menu_list = ['Открыть телефонную книгу.',
                 'Показать все контакты.',
                 'Создать контакт.',
                 'Найти контакт.',
                 'Изменить контакт.',
                 'Удалить контакт.',
                 'Сохранить изменения.',
                 'Выход из телефонной книги.',
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')

    return user_input_checking(menu_list, 'Выберите команду: ')


def user_input_checking(data: list, text: str):
    while True:
        try:
            user_input = int(input(text))
            if 1 <= user_input <= len(data):
                return user_input
            else:
                print(f'Введите цифру от 1 до {len(data)}.')
        except ValueError:
            print('Жду цифру!')


def db_success(db: list, check_open: bool):
    if db:
        return True
    elif check_open:
        print('Телефонная книга пустая.')
        return False
    else:
        print('Телефонная книга закрыта.')
        return False


def show_all(db: list, check_open: bool):
    if db_success(db, check_open):
        for i in range(len(db)):
            user_id = i + 1
            print(user_id, *list(v for v in db[i].values()))


def exit_program():
    print('Завершение программы.')
    exit()


def create_contact():
    print('Создание нового контакта: ')
    new_contact = dict()

    list_new = ['lastname', 'firstname', 'phone', 'comment']
    data_new = ['Введите фамилию: ', 'Введите имя: ', 'Введите телефон: ', 'Введите комментарий: ']

    for i in range(4):
        while True:
            try:
                res = input(data_new[i])
                if len(res) == 0:
                    raise Exception
                new_contact[list_new[i]] = res
                break
            except Exception:
                (print('Необходимо ввести хоть какие-то данные!'))

    print('Создан контакт: ')
    print(*list(v for v in new_contact.values()))
    return new_contact


def find_contact(db: list, check_open: bool) -> str:
    if db_success(db, check_open):
        return input('Введите фамилию: ')


def print_contact(data):
    if data:
        for item in data:
            print('\t', *item)
    if data == False:
        print('Такого контакта нет.')


def editing_contact(data) -> str:
    new_data = []
    num_data = 1
    if data == False:
        print('Такого контакта нет.')
    if data:
        if len(data) > 1:
            print('Найдено несколько контактов: ')
            for i in range(len(data)):
                print('\t', i + 1, *data[i])
            num_data = user_input_checking(data, 'Укажите номер контакта для редактирования: ')
            new_data.append(data[num_data - 1])
        else:
            new_data.append(data[0])
        for k, v in (list(enumerate(data[num_data - 1], 1))):
            print('\t', k, v)

        num_edit = user_input_checking(data[num_data - 1], 'Выберите номер поля для редактирования: ')
        new_data.append(data[num_data - 1][num_edit - 1])
        new_data.append(input('Введите новые данные: '))
        return new_data


def few_delete(data: list) -> list:
    new_data = []
    print('Найдено несколько контактов: ')
    for i in range(len(data)):
        print('\t', i + 1, *data[i])
    num_delete = user_input_checking(data, 'Укажите номер контакта, который хотите удалить: ')
    new_data.append(data[num_delete - 1])
    return new_data


def print_check_diff():
    print('Даные не сохранены.')
    print('1. Сохранить и выйти.')
    print('2. Выйти без сохранения.')

    user_input = user_input_checking([0, 1], 'Выберете дальнеейшее действие: ')

    return user_input


def check_open_db():
    print('Телефонная книга уже открыта!')
