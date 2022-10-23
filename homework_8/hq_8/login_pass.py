def bd_lp(base):
    global bd_list
    bd_list = list()
    bd_tel = list()
    with open(base, 'r', encoding='utf-8') as bd:
        for line in bd.readlines():
            bd_tel.append(line)
        for i in range(len(bd_tel)):
            bd_list.append(bd_tel[i])
    return bd_list


def authorization(l, p, bas):

    bd_lp(bas)
    for i in range(len(bd_list)):
        if bd_list[i] == l+'\n':
            if bd_list[i+1] == p+'\n':
                return True


def aut_n(l, bas):

    bd_lp(bas)
    for i in range(len(bd_list)):
        if bd_list[i] == l+'\n':
            return bd_list[i+1]
