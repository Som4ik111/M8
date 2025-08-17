import telebot
import os
import random

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7808813003:AAHwxaDYLW4NFEwu9tMo3o5TG8mgplO6gOY")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Я умею такие команды как: /list(Выдает список команд которые рассказывают, что делать при определенном случае.), /mem(Выдает случайный поучительный мем по теме - Лесные пожары.)")

@bot.message_handler(commands=['list'])
def send_list(message):
    bot.reply_to(message, "Команды для определённых случаев:")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    file_list = os.listdir("mems")
    img_name = random.choice(file_list)
    with open(f'mems/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# Запускаем бота
bot.remove_webhook()
bot.polling()