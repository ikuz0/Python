'''Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет'''

print('Введите число')
day = int(input())
if 0 < day < 6:
    print('Нет')
elif 5 < day < 8:
    print('Да')
else:
    print('Число вне диапазона значений!')
