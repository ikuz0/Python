'''Напишите программу, 
которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21'''


print('Введите координаты точки А(Х,У):')
print('А(X: ')
ax = int(input())
print(f'А({ax},Y: ')
ay = int(input())
print('Введите координаты точки B(Х,У):')
print('B(X: ')
bx = int(input())
print(f'B({bx},Y: ')
by = int(input())
print(f'A({ax};{ay}), B({bx};{by})')
print(f'расстояние между точками: {(((bx-ax)**2)+((by-ay)**2))**0.5}')
