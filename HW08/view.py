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


def choice_class():
    print()
    print('Выбор класса:')
    class_list = ['7A', '7B']
    for i in range(len(class_list)):
        print(f'\t{i + 1}. {class_list[i]}')

    number_class = user_input_checking(class_list, 'Выберите класс: ')
    print(f'Выбран класс: {class_list[number_class - 1]}')

    return class_list[number_class - 1]


def choice_subject(db: dict):
    print()
    print('Выбор предмета:')
    subject_list = [k for k in db.keys()]
    for i in range(len(subject_list)):
        print(f'\t{i + 1}. {subject_list[i]}')

    user_choice = user_input_checking(subject_list, 'Выберите предмет: ')
    print(f'Выбран предмет: {subject_list[user_choice - 1]}')

    return subject_list[user_choice - 1]


def main_menu() -> int:
    print()
    print('Меню:')
    menu_list = ['Отобразить список учеников по выбранному предмету.',
                 'Посмотреть оценки ученика по выбранному предмету.',
                 'Выбор ученика для вызова к доске.',
                 'Исправить последнюю оценку ученика по выбранному предмету.',
                 'Изменить предмет.',
                 'Посмотреть успеваемость учеников по всем предметам.',
                 'Сохранить изменения.',
                 'Выход из журнала.',
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')

    return user_input_checking(menu_list, 'Выберите команду: ')


def print_students(list_students: list, subject: str):
    print(f'Список учеников по предмету "{subject}":')
    for i in range(len(list_students)):
        print(f'\t{i + 1} {list_students[i]}')


def choice_student(list_students: list):
    for i in range(len(list_students)):
        print(f'\t{i + 1} {list_students[i]}')

    number_student = user_input_checking(list_students, 'Выберите ученика: ')
    print(f'Выбран ученик: {list_students[number_student - 1]}.')
    return list_students[number_student - 1]


def print_grades(subject: str, name_student: str, gradies: list):
    print(f'Оценки ученика "{name_student}" по предмету "{subject}":')
    print(*gradies)


def stunent_board(name_student: str):
    print(f'К доске идет {name_student}. Вы уверены?')
    check_board = user_input_checking([1, 2], 'Если ДА введите 1, если НЕТ - 2: ')
    return check_board


def grade_edit(subject: str, name_student: str, gradies: list):
    print(f'Оценки ученика "{name_student}" по предмету "{subject}":')
    print(*gradies)
    last_grade = gradies[len(gradies) - 1]
    new_grade = '-1'
    check_grade = '0'
    while not new_grade == check_grade:
        new_grade = input(f'Последняя оценка: "{last_grade}". Укажите новую оценку: ')
        if new_grade == last_grade:
            print(f'Вы хотите "{last_grade}" исправить на "{new_grade}"? Повнимательнее!')
            return False
        check_grade = input(f'Для того чтобы занести в журнал оценку "{new_grade}", продублируйте ее еще раз": ')

    return new_grade


def new_grade(name_student: str):
    grade = '1'
    check_grade = '0'
    while not grade == check_grade:
        grade = input(f'На какую оценку ответил ученик {name_student}? ')
        check_grade = input(f'Для того чтобы занести в журнал оценку "{grade}", продублируйте ее еще раз": ')

    print(f'Оценка "{grade}" добавлена ученику: {name_student}.')
    return grade


def print_all_students_gradies(db: dict):
    for k1, v1 in db.items():
        print(f'\tОценки по предмету "{k1}":')
        for k2 in v1.keys():
            print(f'\t\t{k2.ljust(22)} {(" ".join(v1.get(k2)))}')
        print()


def check_diff():
    print('Внесенные оценки не сохранены.')
    print('1. Сохранить и выйти.')
    print('2. Выйти без сохранения.')

    user_input = user_input_checking([0, 1], 'Выберете дальнеейшее действие: ')

    return user_input


def exit_program():
    print('Завершение программы.')
    exit()
