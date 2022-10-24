
def gr_grade(fille):
    global bd_list
    subject = fille
    bd_list = list()
    bd_tel = list()
    with open(subject, 'r', encoding='utf-8') as bd:
        for line in bd.readlines():
            bd_tel.append(line)
        for i in range(len(bd_tel)):
            bd_list.append(bd_tel[i])
    return bd_list


def add_grade(name, grade, fille):
    al = list()
    global bd_olist
    f = open(fille, 'w', encoding='utf-8')

    bd_olist = list()
    grade1 = ' '+grade
    for i in range(len(bd_list)):
        o_list = str(bd_list[i]).replace('\n', '')
        bd_olist.append(o_list)

    for i in range(len(bd_olist)):
        if bd_olist[i] == name:
            bd_olist[i+1] = bd_olist[i+1]+grade1

    for i in range(len(bd_olist)):
        if bd_olist[i] == name:
            print(f'{bd_olist[i]}\n{bd_olist[i+1]}')

    for i in range(len(bd_olist)):
        al.append(str(bd_olist[i])+'\n')
    f.writelines(al)
    f.close


def stud_list(name, fille):
    gr_grade(fille)
    bd_olist = list()

    o_list = ''
    for i in range(len(bd_list)):
        o_list = str(bd_list[i]).replace('\n', '')
        bd_olist.append(o_list)

    for i in range(len(bd_olist)):
        if bd_olist[i] == name:
            print(f'{bd_olist[i]}\n{bd_olist[i+1]}')
    return bd_olist


def homework(sub, grup, fille):
    hw_list = list()
    gr_grade(fille)
    for i in range(len(bd_list)):
        hw_ = str(bd_list[i]).replace('\n', '')
        hw_list.append(hw_)
    if sub == 'ist':
        s = 1
    elif sub == 'match':
        s = 3
    elif sub == 'rus':
        s = 5
    for i in range(0, len(hw_list)-2):
        if hw_list[i] == str(grup):
            if hw_list[i+s] == sub:
                print(f'Ответ->{hw_list[i+s]}\n{hw_list[i+s+1]}')


def homework_add(sub, grup, fille, work):
    gr_grade(fille)
    hw_list = list()
    al = list()
    work_add = '| ' + work
    f = open(fille, 'w', encoding='utf-8')
    for i in range(len(bd_list)):
        hw_ = str(bd_list[i]).replace('\n', '')
        hw_list.append(hw_)

    if sub == 'ist':
        s = 1
        name = 'История'
    elif sub == 'match':
        s = 3
        name = 'Математика'
    elif sub == 'rus':
        s = 5
        name = 'Русский язык'

    for i in range(0, len(hw_list)-2):
        if hw_list[i] == str(grup):
            if hw_list[i+s] == sub:
                hw_list[i+s+1] = hw_list[i+s+1]+work_add
                print(f'{name}\n{hw_list[i+s+1]}')

    for i in range(len(hw_list)):
        al.append(str(hw_list[i])+'\n')
    f.writelines(al)
    f.close


def hw_stud(num):

    hw_list = list()
    gr_grade('hw.txt')
    for i in range(len(bd_list)):
        hw_ = str(bd_list[i]).replace('\n', '')
        hw_list.append(hw_)
    for i in range(0, len(hw_list)-2):
        if hw_list[i] == str(num):
            print(
                f'История:\n{hw_list[i+2]}\nМатематика:\n{hw_list[i+4]}\nРусский язык:\n{hw_list[i+6]}')


def stud_list_(name, fille):
    gr_grade(fille)
    bd_olist = list()

    o_list = ''
    for i in range(len(bd_list)):
        o_list = str(bd_list[i]).replace('\n', '')
        bd_olist.append(o_list)

    if fille == 'ist.txt':
        nam = 'История'
    elif fille == 'match.txt':
        nam = 'Математика'
    elif fille == 'rus.txt':
        nam = 'Русский язык'
    for i in range(len(bd_olist)):
        if bd_olist[i] == name:
            print(f'{nam}\n{bd_olist[i+1]}')
