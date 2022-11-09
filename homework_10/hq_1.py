# Калькулятор рациональных и комплексных чисел, добавить систему логирования


import telebot.types
from telebot import TeleBot, types
from datetime import datetime as dt

bot = TeleBot('5498581242:AAF1bnFZdJAJTYqZzf96Uc_PsTqF834PtrQ')

with open('log.txt', 'a', encoding='utf-8')as f_log:
    time = dt.now().strftime('%d/%m/%y %H:%M')
    f_log.write('\n{} /Бот запущен/'.format(
        time))


def calc(message):
    lst = message.split()
    st1 = complex(str(lst[0]))
    st2 = complex(str(lst[1]))
    result = str(st1+st2)
    return result


def log(data, user_id):
    time = dt.now().strftime('%d/%m/%y %H:%M')
    file = open('log.txt', 'a', encoding='utf-8')
    file.write('\n{} /Пользователь id: {}/Введено значение: {}'.format(
        time, user_id, data))
    file.close()


@bot.message_handler(commands=['complex'])
def start_command(msg: telebot.types.Message):
    log(msg.text, msg.from_user.id)
    bot.send_message(chat_id=msg.from_user.id,
                     text='Введите строку через пробел\nпример:\n5+6j 7-8j')
    bot.register_next_step_handler(callback=add_us, message=msg)


def add_us(msg: telebot.types.Message):
    log(msg.text, msg.from_user.id)
    bot.send_message(chat_id=msg.from_user.id, text=calc(msg.text))


@bot.message_handler(commands=['log'])
def loging(msg: telebot.types.Message):
    log(msg.text, msg.from_user.id)
    bot.send_message(chat_id=msg.from_user.id,
                     text='Экспорт log ')
    bot.send_document(chat_id=msg.from_user.id,
                      document=open('log.txt', 'rb'))


@bot.message_handler(commands=['help'])
def help_command(msg: telebot.types.Message):
    log(msg.text, msg.from_user.id)
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Выберите действие:\n/complex - запустить калькулятор\n/log- получить лог действий ')


@bot.message_handler(commands=['start'])
def start_command(msg: telebot.types.Message):
    log(msg.text, msg.from_user.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start = types.KeyboardButton('/log')
    help = types.KeyboardButton('/help')
    comp = types.KeyboardButton('/complex')
    markup.add(start, help, comp)
    bot.send_message(msg.from_user.id,
                     f' Выберите действие:', reply_markup=markup)


@ bot.message_handler()
def echo(msg: telebot.types.Message):
    log(msg.text, msg.from_user.id)
    bot.send_message(chat_id=msg.from_user.id,
                     text=f' Выберите действие:')

    pass


bot.polling()
