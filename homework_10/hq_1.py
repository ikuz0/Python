# Калькулятор рациональных и комплексных чисел, добавить систему логирования


import telebot.types
from telebot import TeleBot
from datetime import datetime as dt
bot = TeleBot('5498581242:AAF1bnFZdJAJTYqZzf96Uc_PsTqF834PtrQ')

with open('log.txt', 'a', encoding='utf-8')as f_log:
    time = dt.now().strftime('%d/%m/%y %H:%M')
    f_log.write('\n{} /Бот запущен/'.format(
        time))


def menu_item(arg, user_id):
    if arg.isdigit() != True:
        log(arg, user_id)
        return f'Ошибка!! Введено значение: {arg}'
    return arg


def log(data, user_id):
    time = dt.now().strftime('%d/%m/%y %H:%M')
    file = open('log.txt', 'a', encoding='utf-8')
    file.write('\n{} /Пользователь: {}/ Ошибка! Введено значение: {}'.format(
        time, user_id, data))
    file.close()


@bot.message_handler(commands=['log'])
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Экспорт log ')
    bot.send_document(chat_id=msg.from_user.id,
                      document=open('log.txt', 'rb'))


@bot.message_handler(commands=['help'])
def start_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Выберите действие:\n/start - запустить калькулятор\n/log- получить лог ошибок ')


@ bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=f' {menu_item(msg.text,msg.from_user.id)}')
    pass


bot.polling()
