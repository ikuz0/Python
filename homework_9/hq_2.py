import telebot.types
from telebot import TeleBot

bot = TeleBot('5498581242:AAF1bnFZdJAJTYqZzf96Uc_PsTqF834PtrQ')


@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f"Вы прислали: {msg.text}")
    pass


bot.polling()
