from email import message
import telebot
from telebot import TeleBot, types
from datetime import datetime as dt

bot = TeleBot('5498581242:AAF1bnFZdJAJTYqZzf96Uc_PsTqF834PtrQ')

value = ''
old_value = ''
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('j', callback_data='j'),
             telebot.types.InlineKeyboardButton('C', callback_data='C'),
             telebot.types.InlineKeyboardButton('<=', callback_data='<='),
             telebot.types.InlineKeyboardButton('/', callback_data='/'))
keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('*', callback_data='*'))
keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('-', callback_data='-'))
keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('+', callback_data='+'))
keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data=' '),
             telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton(',', callback_data='.'),
             telebot.types.InlineKeyboardButton('=', callback_data='='))

with open('log.txt', 'a', encoding='utf-8')as f_log:
    time = dt.now().strftime('%d/%m/%y %H:%M')
    f_log.write('\n{} /Бот запущен/'.format(
        time))


def log(data, user_name, user_id):
    time = dt.now().strftime('%d/%m/%y %H:%M')
    file = open('log.txt', 'a', encoding='utf-8')
    file.write('\n{}| Пользователь: {}| id: {}| Введено значение: {}'.format(
        time, user_name, user_id, data))
    file.close()


def compl(val):
    i_str = []
    s = ''
    i_real = ''
    i_imag = ''
    de = []
    for i in range(len(value)):
        if value[i] not in ['+', '-']:
            s = s+value[i]
        else:
            i_str.append(s)
            s = ''
            if value[i] == '-':
                s = '-'
            else:
                i_str.append(value[i])
    i_str.append(s)

    for i in range(len(i_str)):
        if str(i_str[i]) == '':
            de.append(i)
    for i in range(len(de)):
        i_str.pop(de[i])

    for i in range(len(i_str)):
        st = str(i_str[i])
        if st.find('j') == -1:
            if i_str[i] != '':
                if i_str[i] != '+':
                    i_real = i_real+'+'+i_str[i]
        else:
            if st[0] != '-':
                i_imag = i_imag+'+'+i_str[i]
            else:
                i_imag = i_imag+i_str[i]

    if i_imag.find('j') == 1:
        i_imag = i_imag.replace('j', '1', 1)
    i_imag = i_imag.replace('j', '')

    if len(i_imag) == 0:
        i_imag = '0'
    if len(i_real) == 0:
        i_real = '0'
    i_imag = eval(i_imag)
    i_real = eval(i_real)

    return f'{complex(i_real, i_imag)}'


@bot.message_handler(commands=['loger'])
def loging(msg: telebot.types.Message):
    log(msg.text, msg.from_user.first_name, msg.from_user.id)
    bot.send_message(chat_id=msg.from_user.id,
                     text='Экспорт истории ввода ')
    bot.send_document(chat_id=msg.from_user.id,
                      document=open('log.txt', 'rb'))


@bot.message_handler(commands=['help'])
def help_command(msg: telebot.types.Message):
    log(msg.text, msg.from_user.first_name, msg.from_user.id)
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Выберите действие:\n/start - запустить калькулятор\n/loger- получить историю действий ')


@ bot.message_handler(commands=['start'])
def echo(msg):

    global value

    if value == '':
        bot.send_message(msg.from_user.id, '0', reply_markup=keyboard)

    else:

        bot.send_message(msg.from_user.id, value, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_func(query):
        global value, old_value
        i_real = []
        i_imag = []
        i_str = []
        data = query.data

        if data == 'no':
            pass
        elif data == 'C':
            value = ''
        elif data == '<=':
            if value != '':
                value = value[:len(value)-1]
        elif data == '=':
            log(value, msg.from_user.first_name, msg.from_user.id)
            if value.find('i') != -1:
                value = compl(value)

            try:
                value = str(eval(value))
            except:
                value = 'ошибка'
        else:
            value += data

        if (value != old_value and value != '') or ('0' != old_value and value == ''):
            if value == '':
                bot.edit_message_text(chat_id=query.message.chat.id,
                                      message_id=query.message.message_id, text='0', reply_markup=keyboard)
                old_value = '0'
            else:
                bot.edit_message_text(chat_id=query.message.chat.id,
                                      message_id=query.message.message_id, text=value, reply_markup=keyboard)
                old_value = value

        if value == 'ошибка':
            value = ''


bot.polling()
