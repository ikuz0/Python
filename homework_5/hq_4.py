'''Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
oooofff111===
4o3f313='''


def coding(s):
    n = str(s[0])
    s_len = 1
    coder = list()
    for i in range(1, len(s)):
        if s[i] == n:
            s_len = s_len+1
            n = s[i]
            if s_len == 9:
                coder.append(str(s_len))
                s_len = 0
                coder.append(str(n))
                n = s[i]
        else:
            coder.append(str(s_len))
            s_len = 1
            coder.append(str(n))
            n = s[i]
    coder.append(str(s_len))
    coder.append(str(n))
    for i in range(len(coder)):
        print(coder[i], end='')


def decoder(s):
    dec = list()
    for i in range(0, len(s)-1, 2):
        dec.append(str(s[i+1])*int(s[i]))
    for i in range(len(dec)):
        print(dec[i], end='')


ff = False
while ff != True:
    print('Выберите режим работы:\n 1 - для кодирования \n 2 - для восстановления')
    num = int(input())
    if num == 1:
        print('Введите строку: ')
        s1 = input()
        coding(s1)
        ff = True
    elif num == 2:
        print('Введите строку: ')
        s1 = input()
        decoder(s1)
        ff = True
    else:
        print('выбран неверный режим работы')
