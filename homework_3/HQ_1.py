'''Задайте список из нескольких чисел. 
Напишите программу, 
которая найдёт сумму элементов списка, 
стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, 
ответ: 12'''
import random


def ad(ni):
    for i in range(0, ni):
        n.append(random.randint(-20, 20))


def su(ns):
    s = 0
    for i in range(1, ns, 2):
        s += n[i]
    print(f'сумма>> {s}')


n = list()
print('Введите кол-во элементов')
num = int(input())
ad(num)
print(n)
su(num)
