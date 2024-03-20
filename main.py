import telebot
from telebot import types

def read_token_from_file(filename='token.txt'):
    with open(filename, 'r') as file:
        token = file.read().strip()
        return token

TOKEN_API = read_token_from_file()

bot = telebot.TeleBot('TOKEN_API')


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    podrob = types.KeyboardButton('Подробнее')
    register = types.KeyboardButton('Регистрация')
    keyboard.add(podrob, register)

    photo = open('start.png', 'rb')  # Укажите путь к вашему фото
    caption = (f"Привет, {message.from_user.first_name}! Я робот партнерской программы *\"Свой в Альфа Банке\"*.\n\n"
               f"Меня очень радует, твоя заинтересованность данной программой.\n\n"
               f"Рассказать подробнее, или сразу перейти к регистрации?")
    bot.send_photo(message.chat.id, photo, caption=caption, parse_mode='Markdown', reply_markup=keyboard)


@bot.message_handler()
def ans(message):
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        Yes = types.KeyboardButton('ДА')
        No = types.KeyboardButton('НЕТ')
        keyboard.add(Yes, No)
        textofpodrob = ("Проект *«Свой в Альфа»* это партнерская программа, на "
                        "которой *без вложений* можно зарабатывать деньги.\n\n"
                        "Все что нужно - это привести человека в систему, "
                        "предложив ему один из продуктов (дебетовая карта, ОСАГО, КАСКО и др.). "
                        "Процент от его расходов в виде дохода будет возвращаться "
                        "тому, по чьей рекомендации клиент пришел.\n\n"
                        "Регистрируемся?")
        bot.send_message(message.chat.id, textofpodrob, parse_mode="Markdown", reply_markup=keyboard)
    elif message.text == "Регистрация" or message.text.lower() == "да":
        photo = open('reg.png', 'rb')

        text1=("Для начала нужно оформить бесплатную дебетовую карту Альфа банка \"Для своих\".\n\n"
              "Даже, если Вы уже являетесь действующим клиентом Альфа банка, "
              "оформив данную карту у Вас откроются дополнительные категории кэшбэка. Также за оформление данной карты Вы получите бонус 500 рублей.")
        kb=types.InlineKeyboardMarkup()
        kb2=types.InlineKeyboardMarkup()
        url=types.InlineKeyboardButton(text="Оформить карту", url="https://alfasvoy.ru/card")
        kb.add(url)

        bot.send_photo(message.chat.id, caption=text1, photo=photo, reply_markup=kb)

        text2=("После того, как карта оформлена, можно начать проходить регистрацию в проекте, для этого"
               "нажми кнопку \"Зарегестрироваться\" ")
        url = types.InlineKeyboardButton(text="Зарегестрироватсья", url="https://alfasvoy.ru/registration")
        kb2.add(url)

        bot.send_message(message.chat.id, text2, reply_markup=kb2)
    elif message.text.lower() == "нет":
        text=(f"{message.from_user.first_name}, если имеются сомнения, или нужно больше информации о проекте, "
              f"перейди на сайт https://alfasvoy.ru, "
              f"и изучи всё подробно. Либо пиши мне в ЛС, я отвечу на все вопросы и развею твои сомнения.")
        kb=types.InlineKeyboardMarkup()
        url=types.InlineKeyboardButton(text="Перейти на сайт", url="https://alfasvoy.ru/")
        ls=types.InlineKeyboardButton(text="Написать в ЛС", url="https://t.me/bestalfasvoy")
        kb.add(url,ls)

        bot.send_message(message.chat.id,text,reply_markup=kb)



bot.polling(none_stop=True)
