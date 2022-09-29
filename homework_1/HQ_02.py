'''Напишите программу для. проверки истинности утверждения
 ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
     or            and
 для всех значений предикат.'''


print('x  y  z  F1  F2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(
                f'{x}  {y}  {z}   {int(not (x or y or z))}   {int(not (x) and (not (y)) and (not (z)))}')
