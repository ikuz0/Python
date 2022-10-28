import telebot.types
from telebot import TeleBot

bot = TeleBot('5498581242:AAF1bnFZdJAJTYqZzf96Uc_PsTqF834PtrQ')


def addin(text):
    lst = text.split()
    bd_1 = list()
    bd_2 = list()
    if len(lst) == 4:
        with open('book.txt', 'r', encoding='utf-8') as bd:
            for line in bd.readlines():
                bd_1.append(line)
            for i in range(len(bd_1)):
                bd_2.append(bd_1[i])
        for i in range(4):
            bd_2.append(str(lst[i])+'\n')
        f = open('book.txt', 'w', encoding='utf-8')
        bd_2.append('\n')
        f.writelines(bd_2)
        f.close

        return f'выберите действие'
    else:
        return f'Это некоректный запрос{len(lst)}'


@bot.message_handler(commands=['help'])
def start_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Выберите действие:\n/print - Просмотр записей\n/add - Добавление записей\n/export-Экспорт записей\n/import-Импорт записей ')


@bot.message_handler(commands=['add'])
def start_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Введите Фамилию, Имя, Телефон и описание через пробел')
    bot.register_next_step_handler(callback=add_us, message=msg)


def add_us(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=addin(msg.text))


@bot.message_handler(commands=['print'])
def start_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=prin())


@bot.message_handler(commands=['import'])
def start_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='для импорта данных загрузите файл формата "txt"\nФормат данных в файле для импорта:\nФамилия1\nИмя1\nТелефон\nОписание1\nПустая строка(обязательно)\nФамилия2\nИмя2\nТелефон2\nОписание2')


def prin():
    bd_1 = list()
    st = ''
    with open('book.txt', 'r', encoding='utf-8') as bd:
        for line in bd.readlines():
            bd_1.append(line)
        for i in range(len(bd_1)):
            st = st + str(bd_1[i])
    return st


@bot.message_handler(content_types=['document'])
def hello(msg: telebot.types.Message):
    bd_1 = list()
    bd_2 = list()
    bd_ = list()
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open(msg.document.file_name, 'wb') as f_out:
        f_out.write(downloaded_file)
    with open(msg.document.file_name, 'r', encoding='utf-8') as bd:
        for line in bd.readlines():
            bd_1.append(line)
    with open('book.txt', 'r', encoding='utf-8') as bd:
        for line in bd.readlines():
            bd_2.append(line)
    for i in range(len(bd_1)):
        bd_2.append(str(bd_1[i]))
    f = open('book.txt', 'w', encoding='utf-8')
    bd_2.append('\n')
    f.writelines(bd_2)
    f.close


@bot.message_handler(commands=['export'])
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Экспорт телефонной книги ')
    bot.send_document(chat_id=msg.from_user.id,
                      document=open('Book.txt', 'rb'))


@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'выберите пункт меню: ')
    pass


bot.polling()
