'''Задайте число. 
Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] '''


def fib(n):
    for i in range(2, n+1):
        flist.append(flist[i-1]+flist[i-2])
    return flist


def nfib(n):

    for i in range(2, n):
        nflist.append(nflist[i-2]-nflist[i-1])
    nflist.reverse()
    return nflist


def alist():
    fl = len(flist)
    nfl = len(nflist)
    for i in range(0, nfl):
        a.append(nflist[i])
    for i in range(0, fl):
        a.append(flist[i])


a = list()
flist = [0, 1]
nflist = [1, -1]
print('Введите k: ')
k = int(input())
fib(k)
nfib(k)
alist()
print(a)
