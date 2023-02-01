import view
import model


def input_handler(choice: int):
    match choice:
        case 1:
            view.print_students(model.find_students(model.get_db(), model.get_subject()), model.get_subject())
        case 2:
            name_student = view.choice_student(model.find_students(model.get_db(), model.get_subject()))
            gradies = model.find_grades(model.get_db(), model.get_subject(), name_student)
            view.print_grades(model.get_subject(), name_student, gradies)
        case 3:
            check_board = 2
            name_student = ''
            while check_board == 2:
                name_student = view.choice_student(model.find_students(model.get_db(), model.get_subject()))
                check_board = view.stunent_board(name_student)
            model.add_grade(model.get_db(), model.get_subject(), name_student, view.new_grade(name_student))
        case 4:
            name_student = view.choice_student(model.find_students(model.get_db(), model.get_subject()))
            gradies = model.find_grades(model.get_db(), model.get_subject(), name_student)
            new_grade = view.grade_edit(model.get_subject(), name_student, gradies)
            if new_grade:
                model.last_grade_edit(model.get_db(), model.get_subject(), name_student, new_grade)
        case 5:
            model.set_subject(view.choice_subject(model.get_db()))
        case 6:
            view.print_all_students_gradies(model.get_db())
        case 7:
            model.write_db(model.get_db(), model.get_class())
        case 8:
            if model.check_difference(model.get_class(), model.get_db()):
                view.exit_program()
            else:
                user_input = view.check_diff()
                if user_input == 1:
                    model.write_db(model.get_db(), model.get_class())
                    view.exit_program()
                else:
                    view.exit_program()


def start():
    model.set_class(view.choice_class())
    model.read_db(model.get_class())
    model.set_subject(view.choice_subject(model.get_db()))
    model.find_students(model.get_db(), model.get_subject())
    while True:
        input_handler(view.main_menu())
