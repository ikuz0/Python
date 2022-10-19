import logger as lg
import adding as ad


def menu():
    while True:
        print('Выберите действие: \n')
        print('1 - Просмотр записей')
        print('2 - Добавление записи')
        print('3 - Экспорт записей')
        print('4 - Импорт записей')
        print('5 - Завершить программу\n')
        n = menu_item(input('Выберите пункт меню: '))
        if n == 1:
            print(ad.bd_list)
            print('для возврата в меню введите 6:')
            n = menu_item(input())
        elif n == 2:
            print('Добавление записей')
        elif n == 3:
            print('Экспорт')
        elif n == 4:
            print('Импорт')
            ad.add_bd()
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
