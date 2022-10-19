

def add_bd():
    bd_tel = list()
    global bd_list
    with open('directory.txt', 'r', encoding='utf-8') as bd:
        for line in bd.readlines():
            bd_tel.append(line)
    bd_list = ''.join(map(str, bd_tel))
    print(bd_list)
