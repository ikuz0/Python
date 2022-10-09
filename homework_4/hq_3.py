'''Задайте последовательность чисел. 
Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]'''


def numbers(n):
    for i in range(len(n)):
        if n[i].isdigit() == True:
            a.append(n[i])
    return a


def unique():
    auniq = list()
    for i in range(0, len(a)):
        s = 0
        for j in range(0, len(a)):
            if a[i] == a[j]:
                s += 1
        if s == 1:
            auniq.append(a[i])
    print(f'Неповторяющиеся элементы >> {auniq}')


a = list()
print('Введите последовательность: ')
num = input()
numbers(num)
print(f'входная последовательность >> {a}')
unique()
