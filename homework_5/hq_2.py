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


from ast import While
import random

stones = 57


print('Введите имя 1го игрока: ')
name_1 = input()
print('Введите имя 2го игрока: ')
name_2 = input()

# lottery = random.randint(0, 100)
# print(lottery)
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
        print(f'{name_2} Выиграл!')
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
            print(f'{name_1} Выиграл!')
            break
