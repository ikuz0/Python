'''Задание 1 Напишите программу,
 которая принимает на вход вещественное число 
 и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11'''


def sum(n):
    sumnum = 0
    for i in range(len(n)):
        if n[i] != '.':
            sumnum += int(n[i])
    print(f'Сумма цифр: {sumnum}')


print('Введите число: ')
number = input()
sum(number)
