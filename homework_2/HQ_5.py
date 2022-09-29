'''Задание 5 Реализуйте алгоритм перемешивания списка.'''
import random


def nlist(nl):
    for i in range(1, nl+1):
        n.append(random.randint(-20, 20))


def nrandom(num):
    for i in range(num):
        j = random.randint(1, num-1)
        numb = n[i]
        n[i] = n[j]
        n[j] = numb


n = list()
print('Введите колличество элементов:')
num = int(input())

nlist(num)
print(n)
nrandom(num)
print(n)
