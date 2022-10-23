import login_pass as lo


def menu():
    while True:
        print('логин')
        login = input()
        print('Пароль')
        password = input()
        if lo.authorization(login, password) == True:
            print('Здравствуйте студент')
            break
        else:
            print('Неверный логин или пароль\nПовторите ввод')

    # while True:
    #     print('Выберите действие:')
    #     print('1 - Показть список групп')
    #     print('2 - Показать расписание на неделю')
    #     print('3 - Добавление Д/з и оценок')
    #     n = menu_item(input())
    #     break


def menu_item(arg):
    while arg.isdigit() != True:

        print('\n Не верный ввод')
        arg = input('Выберите пункт меню: ')
    return int(arg)


menu()
