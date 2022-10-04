'''Напишите программу, 
которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент,
второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''
import random


def ad(ni):
    for i in range(0, ni):
        n.append(random.randint(-20, 20))


def av(na):
    for i in range(0, na):
        if (i < (na/2)):
            s.append(n[i]*n[(na-1)-i])
    print(s)


n = list()
s = list()
print('Введите кол-во элементов')
num = int(input())
ad(num)
print(n)
av(num)
