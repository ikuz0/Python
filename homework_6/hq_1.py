'''Задание 1 Напишите программу,
 которая принимает на вход вещественное число 
 и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11'''

'''Было'''
# def sum(n):
#     sumnum = 0
#     for i in range(len(n)):
#         if n[i].isdigit() == True:
#             sumnum += int(n[i])
#     print(f'Сумма цифр: {sumnum}')


# print('Введите число: ')
# number = input()
# sum(number)

'''Стало'''
from functools import reduce
print('Введите число')
num = input()
list = [int(num[i]) for i in range(0, len(num), 1) if num[i].isdigit() == True]
sum = reduce((lambda x, y: x+y), list)
print(sum)
