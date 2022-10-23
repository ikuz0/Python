def bd_lp():
    global bd_list
    bd_list = list()
    bd_tel = list()
    with open('login_password.txt', 'r', encoding='utf-8') as bd:
        for line in bd.readlines():
            bd_tel.append(line)
        for i in range(len(bd_tel)):
            bd_list.append(bd_tel[i])
    return bd_list


def authorization(l, p):

    bd_lp()
    for i in range(len(bd_list)):
        if bd_list[i] == l+'\n':
            if bd_list[i+1] == p+'\n':
                return True
