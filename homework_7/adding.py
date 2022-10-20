
bd_list = list()


def st_bd():
    bd_tel = list()
    global bd_list
    with open('book.txt', 'r', encoding='utf-8') as bd:
        for line in bd.readlines():
            bd_tel.append(line)
        for i in range(len(bd_tel)):
            bd_list.append(bd_tel[i])


def add_bd():
    bd_tel = list()
    global bd_list
    with open('import.txt', 'r', encoding='utf-8') as bd:
        for line in bd.readlines():
            bd_tel.append(line)
        for i in range(len(bd_tel)):
            bd_list.append(bd_tel[i])


def add_us():
    global bd_list
    print('Введите фамилию: ')
    data = input()
    bd_list.append(data+'\n')
    print('Введите Имя: ')
    data = input()
    bd_list.append(data+'\n')
    print('Введите Телефон: ')
    data = input()
    bd_list.append(data+'\n')
    print('Введите Описание: ')
    data = input()
    bd_list.append(data+'\n')
    bd_list.append('\n')
