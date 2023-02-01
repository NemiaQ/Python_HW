db = {}
choice_subject = ''
choice_class = ''


def get_db():
    global db
    return db


def set_db(new_data):
    global db_list
    db_list.append(new_data)


def get_subject():
    global choice_subject
    return choice_subject


def set_subject(subject: str):
    global choice_subject
    choice_subject = subject


def get_class():
    global choice_class
    return choice_class


def set_class(my_class: str):
    global choice_class
    choice_class = my_class + '.txt'


def read_db(path: str):
    db = get_db()
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            student_dict = dict()
            line = line.strip().split(':')
            line2 = line[1].split(';')
            for item in line2:
                name = ''.join([i for i in item if not i.isdigit()])
                grade = [i for i in item if i.isdigit()]
                student_dict[name] = grade
            id = line[0]
            db[id] = student_dict


def find_students(db: dict, subject: str):
    list_students_and_grades = db.get(subject)
    list_students = [k for k in list_students_and_grades.keys()]
    return list_students


def find_grades(db: dict, subject: str, name_student: str):
    list_students_and_grades = db.get(subject)
    for k in list_students_and_grades.keys():
        if k == name_student:
            return list_students_and_grades.get(k)
            # ['5', '4', '3']


def last_grade_edit(db: dict, subject: str, name_student: str, new_grage: str):
    list_students_and_grades = db.get(subject)
    for k in list_students_and_grades.keys():
        if k == name_student:
            list_students_and_grades.get(k)[-1] = new_grage


def add_grade(db: dict, subject: str, name_student: str, grade: str):
    list_students_and_grades = db.get(subject)
    for k, v in list_students_and_grades.items():
        if k == name_student:
            v.append(grade)


def write_db(db: dict, path: str):
    file = open(path, 'w', encoding='UTF-8')
    for k1, v1 in db.items():
        line = k1 + ':'
        for k2, v2 in v1.items():
            line += (k2 + ''.join(v2) + ';')
        file.write(f'{line[:-1]}\n')
    file.close()


def check_difference(path: str, db_new: dict):
    db = {}
    file = open(path, 'r', encoding='UTF-8')
    my_list = file.readlines()
    for line in my_list:
        student_dict = dict()
        line = line.strip().split(':')
        line2 = line[1].split(';')
        for item in line2:
            name = ''.join([i for i in item if not i.isdigit()])
            grade = [i for i in item if i.isdigit()]
            student_dict[name] = grade
        id = line[0]
        db[id] = student_dict
    return (db == db_new)
