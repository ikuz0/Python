import login_pass as lo
import add as a


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
                        print('Расписание группы')
                    elif n == 2:
                        print(' Домашнее задание')
                    elif n == 3:
                        print(' оценки')
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
                        while True:
                            pred = lo.aut_n(login, 'ticher.txt')
                            pr = str(pred).replace('\n', '.txt')
                            print(' Д\з и оценки')
                            print('Выберите действие:')
                            print('1 - добавить оценки')
                            print('2 - добавить домашнее задание')
                            print('0 - Выход в меню')
                            n = menu_item(input())
                            if n == 1:
                                print('Введите Фамилию студента: ')
                                name_stud = input()
                                a.stud_list(name_stud, pr)
                                print('Введите оценку: ')
                                n = menu_item(input())
                                a.add_grade(name_stud, str(n), pr)
                            elif n == 2:
                                pr_hw = str(pred).replace('\n', '')
                                print('Введите номер группы: ')
                                n = menu_item(input())
                                a.homework(pr_hw, n, 'hw.txt')
                                print('Введите задание: ')
                                work = input()
                                a.homework_add(pr_hw, n, 'hw.txt', work)

                            elif n == 0:
                                break

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
