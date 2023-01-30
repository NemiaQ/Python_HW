db_list = []
check_open = False


def get_db():
    global db_list
    return db_list


def set_db(new_data: dict):
    global db_list
    db_list.append(new_data)


def get_check_open():
    global check_open
    return check_open


def set_check_open(check: bool):
    global check_open
    check_open = check


def read_db(path: str):
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            set_db(id_dict)


def find_lastname(lastname):
    if lastname:
        flag = False
        db = get_db()
        find_data = []

        for i in range(len(db)):
            if db[i].get('lastname').lower() == lastname.lower():
                find_data.append(list(v for v in db[i].values()))
                flag = True

        if flag:
            return find_data
        if not flag:
            return False


def editing(data: list) -> list:
    db = get_db()
    for item in db:
        if list(v for v in item.values()) == data[0]:
            for k, v in item.items():
                if v == data[1]:
                    item[k] = data[2]
                    new_data = []
                    new_data.append(['Данные изменены:'])
                    new_data.append(list(v for v in item.values()))
                    return new_data


def delete_contact(data: list):
    if data:
        db = get_db()
        new_data = []
        for i in range(len(db)):
            if list(v for v in db[i].values()) == data[0]:
                new_data.append(['Контакт удален:'])
                new_data.append(list(v for v in db[i].values()))
                db.pop(i)
                return new_data


def write_db(path: str):
    check_open = get_check_open()
    if check_open:
        db = get_db()
        file = open(path, 'w', encoding='UTF-8')
        for item in db:
            line = list(v for v in item.values())
            data = ';'.join(line)
            file.write(f'{data}\n')
        file.close()


def check_difference(path: str):
    check_open = get_check_open()
    if check_open:
        db = get_db()
        list_db = []
        file = open(path, 'r', encoding='UTF-8')
        my_list = file.readlines()
        for i in range(len(my_list)):
            my_list[i] = my_list[i].strip()
        for item in db:
            data = ';'.join(list(v for v in item.values()))
            list_db.append(data)

        if not list_db == my_list:
            return False
