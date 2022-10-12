'''
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку,
чтобы забрать все конфеты у своего конкурента?
    a) Добавьте игру против бота
    b) Подумайте как наделить бота ""интеллектом""'''


import random

candy = 57    # Начальное колличество конфет


def u_u(stones):
    print('Введите имя 1го игрока: ')
    n_1 = input()
    print('Введите имя 2го игрока: ')
    n_2 = input()

    lottery = random.randint(0, 1)
    if lottery == 1:
        name_1 = n_2
        name_2 = n_1
    else:
        name_1 = n_1
        name_2 = n_2
    print(f'Первым ходит {name_1}')
    while stones > 0:
        f1 = False
        print(f'{name_1} ваш ход: ')
        while f1 != True:
            num_1 = input()
            if num_1.isdigit():
                if 0 < int(num_1) < 29:
                    stones = stones - int(num_1)
                    f1 = True
                else:
                    print(f'Введите числовое значение от 1 до 28')
                    print(f'{name_1} ваш ход: ')
            else:
                print(f'Введите числовое значение от 1 до 28')
                print(f'{name_1} ваш ход: ')

        print(f'осталось {stones}- конфет')
        if stones < 29:
            print(f'{name_2}, Вы выиграли!')
            break
        else:
            f2 = False
            print(f'{name_2} ваш ход: ')
            while f2 != True:
                num_2 = input()
                if num_2.isdigit():
                    if 0 < int(num_2) < 29:
                        stones = stones - int(num_2)
                        f2 = True
                    else:
                        print(f'Введите числовое значение от 1 до 28')
                        print(f'{name_2} ваш ход: ')
                else:
                    print(f'Введите числовое значение от 1 до 28')
                    print(f'{name_2} ваш ход: ')
            print(f'осталось {stones}- конфет')
            if stones < 29:
                print(f'{name_1}, Вы выиграли!')
                break


def u_b(stones):
    lottery = random.randint(0, 1)
    if lottery == 1:
        print('Введите Ваше имя: ')
        name_1 = input()
        while stones > 0:
            f1 = False
            print(f'{name_1} ваш ход: ')
            while f1 != True:
                num_1 = input()
                if num_1.isdigit():
                    if 0 < int(num_1) < 29:
                        stones = stones - int(num_1)
                        f1 = True
                    else:
                        print(f'Введите числовое значение от 1 до 28')
                        print(f'{name_1} ваш ход: ')
                else:
                    print(f'Введите числовое значение от 1 до 28')
                    print(f'{name_1} ваш ход: ')
            print(f'осталось {stones}- конфет')
            if stones < 29:
                print(f'Вы проиграли!!')
                break
            else:
                f2 = False
                print('ход бота')
                while f2 != True:
                    for i in range(1, 29):
                        if (stones - i) % 28 == 1:
                            print(i)
                            nu = i
                            f2 = True
                    stones = stones-nu
                print(f'осталось {stones}- конфет')
                if stones < 29:
                    print(f'{name_1}, Вы выиграли!')
                    break
    else:
        print('Введите Ваше имя: ')
        name_1 = input()
        while stones > 0:
            f2 = False
            print('ход бота')
            while f2 != True:
                for i in range(1, 29):
                    if (stones - i) % 28 == 1:
                        print(i)
                        nu = i
                        f2 = True
                stones = stones-nu
            print(f'осталось {stones}- конфет')
            if stones < 29:
                print(f'{name_1}, Вы выиграли!')
                break
            else:
                f1 = False
                print(f'{name_1} ваш ход: ')
                while f1 != True:
                    num_1 = input()
                    if num_1.isdigit():
                        if 0 < int(num_1) < 29:
                            stones = stones - int(num_1)
                            f1 = True
                        else:
                            print(f'Введите числовое значение от 1 до 28')
                            print(f'{name_1} ваш ход: ')
                    else:
                        print(f'Введите числовое значение от 1 до 28')
                        print(f'{name_1} ваш ход: ')
                print(f'осталось {stones}- конфет')
                if stones < 29:
                    print(f'Вы проиграли!!')
                break


print('выберите вариант игры: \n введите количество игроков \n 1-для игры с ботом \n 2-для игры двух игроков')
num = int(input())
if num == 2:
    u_u(candy)
else:
    print('Игра с ботом')
    u_b(candy)
