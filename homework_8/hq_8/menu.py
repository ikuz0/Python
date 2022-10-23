import login_pass as lo


def menu():
    while True:
        print('Выберите действие:')
        print('1 - Авторизация')
        print('0 - Выход из программы')
        n = menu_item(input())
        if n == 1:
            print('логин')
            login = input()
            print('Пароль')
            password = input()
            if lo.authorization(login, password, 'log_pass_stud.txt') == True:
                names = lo.aut_n(login, 'Student.txt')
                print(f'\nЗдравствуйте, {names} \n')
                while True:
                    print('Выберите действие:')
                    print('1 - Показать расписание на неделю')
                    print('2 - Показать Д/з')
                    print('3 - Показать оценки')
                    print('0 - Выход из программы')
                    n = menu_item(input())
                    if n == 1:
                        print('Список групп')
                    elif n == 2:
                        print(' Расписание')
                    elif n == 3:
                        print(' Д\з и оценки')
                    elif n == 0:
                        print('выход')
                        break
            elif lo.authorization(login, password, 'log_pass_teach.txt') == True:
                names = lo.aut_n(login, 'ticher_names.txt')
                print(f'\nЗдравствуйте, {names}')
                while True:
                    print('\nВыберите действие: ')
                    print('1 - Показть список групп')
                    print('2 - Показать расписание на неделю')
                    print('3 - Добавление Д/з и оценок')
                    print('0 - Выход из программы')
                    n = menu_item(input())
                    if n == 1:
                        print('Список групп: ')
                        lo.bd_lp('Group.txt')
                        g_list = lo.bd_list
                        for i in range(len(g_list)):
                            if g_list[i] != '\n':
                                print(f'{g_list[i]}', end='')
                        print('Для просмотра студентов введите номер группы: ')
                        gr = input()
                        gr_g = gr+'.txt'
                        print(gr_g)
                        lo.bd_lp(gr_g)
                        gr_list = lo.bd_list
                        for i in range(len(gr_list)):
                            print(gr_list[i])
                        gr_list = lo.bd_list
                    elif n == 2:
                        print(' Расписание')
                    elif n == 3:
                        print(' Д\з и оценки')
                    elif n == 0:
                        print('выход')
                        break
            else:
                print('Неверный логин или пароль\nПовторите ввод')
        elif n == 0:
            print('Программа завершена')
            break
        else:
            print('Неверный ввод')


def menu_item(arg):
    while arg.isdigit() != True:

        print('\n Не верный ввод')
        arg = input('Выберите пункт меню: ')
    return int(arg)


menu()
