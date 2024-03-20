import telebot
from telebot import types

bot = telebot.TeleBot('7117333631:AAG6ZEtizz0s10kcZDVTpxqqeKGBi44wifU')


@bot.message_handler(commands=['start'])
def start(message):
    photo = open('D:\Python\ProjectsPYCHARM\Alfasvoy_bot\lol.png', 'rb')  # Укажите путь к вашему фото
    caption = (f"Привет,{message.from_user.first_name}! Я робот партнерской программы *\"Свой в Альфа Банке\"*.\n\n\n"
               f"Меня очень радует, твоя заинтересованность данной программой.\n\n\n"
               f"Рассказать подробнее, или сразу перейти к регистрации?")
    bot.send_photo(message.chat.id, photo, caption=caption, parse_mode='Markdown')





@bot.message_handler()
def markup(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    podrob = types.KeyboardButton('Подробнее')
    register = types.KeyboardButton('Регистрация')
    keyboard.add(podrob, register)
    if message.text == podrob:
        textofpodrob = ("Проект *«Свой в Альфа»* это партнерская программа, на\n"
                        "которой *без вложений* можно зарабатывать деньги.\n\n"
                        "Все что нужно - это привести человека в систему,\n"
                        "предложив ему один из продуктов (дебетовая карта, ОСАГО, КАСКО и др.).\n"
                        "Процент от его расходов в виде дохода будет возвращаться\n"
                        "тому, по чьей рекомендации клиент пришел.\n\n"
                        "Регистрируемся?")
        bot.send_message(message.chat.id, textofpodrob, parse_mode="Markdown", reply_markup=keyboard)


bot.infinity_polling()
