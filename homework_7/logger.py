from datetime import datetime as dt


def log(data):
    time = dt.now().strftime('%d/%m/%y %H:%M')
    file = open('log.txt', 'a', encoding='utf-8')
    file.write('\n{} Ошибка! Введено значение: {}'.format(time, data))
