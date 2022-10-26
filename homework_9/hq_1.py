import emoji

'''Создайте программу для игры в ""Крестики-нолики"".'''


def print_a(a_list):
    for i in range(0, 3):
        print(f'{emoji.emojize(a_list[i])}', end=' | ')
    print()
    for i in range(3, 6):
        print(f'{emoji.emojize(a_list[i])}', end=' | ')
    print()
    for i in range(6, 9):
        print(f'{emoji.emojize(a_list[i])}', end=' | ')
    print()


def win_1(a):
    w = False
    if a[0] == a[1] == a[2] == ':cross_mark:':  # 1строка
        w = True
    elif a[3] == a[4] == a[5] == ':cross_mark:':     # 2
        w = True
    elif a[6] == a[7] == a[8] == ':cross_mark:':     # 3
        w = True
    elif a[0] == a[3] == a[6] == ':cross_mark:':  # 1st
        w = True
    elif a[1] == a[4] == a[7] == ':cross_mark:':  # 2st
        w = True
    elif a[2] == a[5] == a[8] == ':cross_mark:':  # 3st
        w = True
    elif a[0] == a[4] == a[8] == ':cross_mark:':  # diag1
        w = True
    elif a[2] == a[4] == a[6] == ':cross_mark:':  # diag2
        w = True
    return w


def win_2(a):
    w = False
    if a[0] == a[1] == a[2] == ':hollow_red_circle:':  # 1строка
        w = True
    elif a[3] == a[4] == a[5] == ':hollow_red_circle:':     # 2
        w = True
    elif a[6] == a[7] == a[8] == ':hollow_red_circle:':     # 3
        w = True
    elif a[0] == a[3] == a[6] == ':hollow_red_circle:':  # 1st
        w = True
    elif a[1] == a[4] == a[7] == ':hollow_red_circle:':  # 2st
        w = True
    elif a[2] == a[5] == a[8] == ':hollow_red_circle:':  # 3st
        w = True
    elif a[0] == a[4] == a[8] == ':hollow_red_circle:':  # diag1
        w = True
    elif a[2] == a[4] == a[6] == ':hollow_red_circle:':  # diag2
        w = True
    return w


def the_end(a):
    end_ = False
    sum = 0
    for i in range(len(a)):
        if a[i] == ':cross_mark:':
            sum = sum+1
        else:
            if a[i] == ':hollow_red_circle:':
                sum = sum+1
    if sum == 9:
        end_ = True
    return end_


a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print('введите имя первого игрока')
user_name_1 = input()
print('введите имя второго игрока')
user_name_2 = input()
print_a(a)
f = False
while f != True:
    f1 = False
    print(f'{user_name_1} ваш ход: ')
    while f1 != True:
        num_1 = int(input())-1
        if (a[num_1] != ':cross_mark:'):
            if a[num_1] != ':hollow_red_circle:':
                a[num_1] = ':cross_mark:'
                f1 = True
            else:
                print('Поле занято, введите другое значение')
                print(f'{user_name_1} ваш ход: ')
        else:
            print('Поле занято, введите другое значение')
            print(f'{user_name_1} ваш ход: ')
    print_a(a)
    if the_end(a) == True:
        print('Ничья!')
        f = True
    else:
        if win_1(a) == True:
            print(f'{user_name_1}, Вы выиграли!')
            break

        else:
            f2 = False

            print(f'{user_name_2} ваш ход: ')
            while f2 != True:
                num_2 = int(input())-1
                if (a[num_2] != ':cross_mark:'):
                    if a[num_2] != ':hollow_red_circle:':
                        a[num_2] = ':hollow_red_circle:'
                        f2 = True
                    else:
                        print('Поле занято, введите другое значение')
                        print(f'{user_name_2} ваш ход: ')
                else:
                    print('Поле занято, введите другое значение')
                    print(f'{user_name_2} ваш ход: ')
            print_a(a)
            if win_2(a) == True:
                print(f'{user_name_2}, Вы выиграли!')
                break
        if the_end(a) == True:
            print('Ничья!')
            f = True
