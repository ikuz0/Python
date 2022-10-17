'''Задание 3 Задайте список из n чисел
последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.
Пример:
Для n = 6 -> 14.072'''

"""Было"""
# def l(nlis):

#     for i in range(1, nlis+1):
#         n.append((1+(1/i)) ** i)


# def sN(nlis):
#     sum = 0
#     for i in range(len(n)):
#         sum = sum + n[i]
#     print(f'{round(sum,3)}')


# n = list()
# print('Введите число N: ')
# num = int(input())
# l(num)
# print(n)
# sN(num)


'''Стало'''
from functools import reduce
print('Введите число N: ')
num = int(input())
n = [((1+(1/i))**i) for i in range(1, num+1)]
sum = round(reduce((lambda x, y: x+y), n), 3)
print(sum)
