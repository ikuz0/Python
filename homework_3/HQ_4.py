'''Напишите программу,
 которая будет преобразовывать 
 десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10'''


def numBin(n):
    a = list()
    while n > 1:
        m = n % 2
        n = n//2
        a.append(m)
    a.append(n)
    a.reverse()
    for i in range(0, len(a)):

        print(a[i], end='')


print('Введите число: ')
num = int(input())
numBin(num)
