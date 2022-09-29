'''Задание 3 Задайте список из n чисел
последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.
Пример:
Для n = 6 -> 14.072'''


def l(nlis):

    for i in range(1, nlis+1):
        n.append((1+(1/i)) ** i)
    return n


def sumN(nlis):
    sum = 0
    for i in range(len(n)):
        sum = sum + n[i]
    print(f'{round(sum,3)}')


n = list()
print('Введите число N: ')
num = int(input())
l(num)
print(n)
sumN(num)
