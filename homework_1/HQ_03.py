'''Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3'''


print('Введите координату X: ')
x = int(input())
print('Введите координату Y: ')
y = int(input())
print(f'Координтаты точки({x};{y})')
if (x == 0 and y == 0):
    print('Точка в начале координат')
elif (x > 0 and y > 0):
    print('Точка в 1-й четверти')
elif (x < 0 and y > 0):
    print('Точка в 2-й четверти')
elif (x < 0 and y < 0):
    print('Точка в 3-й четверти')
elif (x == 0):
    print('Точка на оси Х')
elif (y == 0):
    print('Точка на оси Y')
else:
    print('Точка в 4-й четверти')
