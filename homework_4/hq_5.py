'''5 Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными. 
Степени многочленов могут отличаться.'''


a1_list = list()
a2_list = list()

with open('new_file_1', 'r', encoding='utf-8') as f1:
    a1 = f1.readlines()
with open('new_file_2', 'r', encoding='utf-8') as f2:
    a2 = f2.readlines()

f1_str = str(a1[0])
f2_str = str(a2[0])

print(f1_str)
max = 0
for i in range(len(f1_str)):
    if f1_str[i] == '^':
        if max < int(f1_str[i+1]):
            max = int(f1_str[i+1])
        print(f'{f1_str[i+1]}')
print(max)
