

def e_bd_phon(data, name):
    fille = open(name, 'w', encoding='utf-8')
    fille.writelines(data)
    fille.close


def e_bd_phon_2(data, name):
    al = list()
    a3 = list()
    a_list = ''
    fille = open(name, 'w', encoding='utf-8')

    for i in range(len(data)):
        al.append(str(data[i]).replace('\n', ';'))

    for i in range(len(al)):
        if al[i] == ';':
            al[i] = '\n'

    fille.writelines(al)
    fille.close
