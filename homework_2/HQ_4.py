'''Задание 4 Задайте список из N элементов, 
заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры.'''


def l(nlis):
    for i in range(-nlis, nlis+1):
        n.append(i)


n = list()
print('Введите N')
N = int(input())
print('Введите a')
a = int(input())
print('Введите b')
b = int(input())
l(N)
print(n)
print(n[a]*n[b])
