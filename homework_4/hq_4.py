''' Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
*Пример:* 
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''
import random


print('Введите натуральную степень k>> ')
num = int(input())
f = open('new_file_hq', 'w', encoding='utf-8')
al = list()
for i in range(num, 0, -1):
    a = random.randint(-10, 20)
    if a > 0:
        al.append('+')
        al.append(str(a))
        al.append(f'X^{i}')
    elif a < 0:
        al.append(str(a))
        al.append(f'X^{i}')
a = random.randint(-10, 20)
if a > 0:
    al.append('+')
    al.append(str(a))
elif a < 0:
    al.append(str(a))

al.append('=0')
f.writelines(al)
f.close()
