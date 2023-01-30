import model
import view


def input_handler(choice: int):
    match choice:
        case 1:
            if not model.get_check_open():
                model.read_db('database.txt')
                model.set_check_open(True)
            else:
                view.check_open_db()

        case 2:
            view.show_all(model.get_db(), model.get_check_open())
        case 3:
            if model.get_check_open():
                model.set_db(view.create_contact())
            else:
                view.db_success(model.get_db(), model.get_check_open())
        case 4:
            view.print_contact(model.find_lastname(view.find_contact(model.get_db(), model.get_check_open())))
        case 5:
            editing_contact = view.editing_contact(
                model.find_lastname(view.find_contact(model.get_db(), model.get_check_open())))
            if editing_contact:
                view.print_contact(model.editing(editing_contact))
        case 6:
            find_delete = model.find_lastname(view.find_contact(model.get_db(), model.get_check_open()))
            if find_delete:
                if len(find_delete) > 1:
                    find_delete = view.few_delete(find_delete)
                view.print_contact(model.delete_contact(find_delete))
            else:
                view.print_contact(find_delete)
        case 7:
            if model.get_check_open():
                model.write_db('database.txt', )
            else:
                view.db_success(model.get_db(), model.get_check_open())
        case 8:
            result = model.check_difference('database.txt')
            if result == False:
                result = view.print_check_diff()
            if result == 1:
                model.write_db('database.txt')
                view.exit_program()
            if result == 2 or result == None:
                view.exit_program()


def start():
    while True:
        user_choice = view.main_menu()
        input_handler(user_choice)
