import logger as lg
import adding as ad
import exp_file as ex


def menu():
    global s_print
    ad.st_bd()
    while True:
        print('Выберите действие: \n')
        print('1 - Просмотр записей')
        print('2 - Добавление записи')
        print('3 - Экспорт записей')
        print('4 - Импорт записей')
        print('5 - Завершить программу\n')

        n = menu_item(input('Выберите пункт меню: '))
        if n == 1:
            s_print = ad.bd_list
            for i in range(len(s_print)):
                print(s_print[i], end='')
            print('для возврата в меню введите любую цифру:')
            n = menu_item(input())
            lg.log(n)
        elif n == 2:
            print('Добавление записей')
            ad.add_us()
            ex.e_bd_phon(s_print, 'book.txt')
        elif n == 3:
            print('Экспорт')
            ex.e_bd_phon(s_print, 'export.txt')
        elif n == 4:
            print('Импорт')
            ad.add_bd()
            ex.e_bd_phon(s_print, 'book.txt')
        elif n == 5:
            print('Работа программы завершена')
            break
        else:
            print('Выбран несуществующий пункт меню')
            lg.log(n)


def menu_item(arg):
    while arg.isdigit() != True:
        lg.log(arg)
        print('\n Не верный ввод')
        arg = input('Выберите пункт меню: ')
    return int(arg)


menu()
