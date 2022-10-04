'''Задайте список из вещественных чисел. 
Напишите программу, 
которая найдёт разницу между максимальным 
и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''
import random


def nlist(ni):
    for i in range(0, ni):
        n.append(round(random.uniform(0, 20), 2))


def slist(ns):
    s = list()
    for i in range(0, ns):
        s.append(round(n[i]-int(n[i]), 2))
    mins = s[0]
    maxs = s[0]
    for i in range(0, ns):
        if (s[i] < mins):
            mins = s[i]
        elif (s[i] > maxs):
            maxs = s[i]
    print(f'=> {maxs-mins}')


n = list()
print('Введите кол-во элементов')
num = int(input())
nlist(num)
print(n)
slist(num)
