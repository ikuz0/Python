''' Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.
*Пример*
- при N=236     ->        [2, 2, 59]'''


def simple_multiplier(n):
    i = 2
    while i*i <= n:
        while (n % i == 0):
            a.append(i)
            n = n/i
        i += 1
    if n > i:
        a.append(int(n))
    print(a)


a = list()
print('Введите число: ')
num = int(input())
simple_multiplier(num)
