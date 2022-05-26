
import telebot
from telebot import types

#5245066688:AAHvGL8FZa9cNN1xWe7SCIbVVurx_1bxiRY

name = ''
surname = ''
age = 0

bot = telebot.TeleBot("5245066688:AAHvGL8FZa9cNN1xWe7SCIbVVurx_1bxiRY")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Оуу, добро пожаловать")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, 'Виделись')
    elif message.text == 'Hi':
        bot.reply_to(message, 'По русски говори блять')
    elif message.text == 'ладно':
        bot.send_message(message.from_user.id, "прохладно, че надо?")
    elif message.text == 'зарегаться':
        bot.send_message(message.from_user.id, "Как звать?")
        bot.register_next_step_handler(message, reg_name)
    elif message.text == 'меня не зовут, я сам прихожу':
        bot.send_message(message.from_user.id, "хааха, ЮМОРИСТ! пошел нахуй отсюда")
        bot.register_next_step_handler(message, reg_name)

	#bot.reply_to(message, message.text)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Как фамилия?")
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Скок лет?")
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global age
    #age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Вводи цифрами блять!") #except нихуя не работает, бот начинает троить, над разобраться 
	


    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе ' + str(age) + '? И тебя зовут: ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text = question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Ну и имя у тебя конечно! Ладно все норм" " " + name + " ""проходи")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Еще раз дятел")
        bot.send_message(call.message.chat.id, "Как звать?")
        bot.register_next_step_handler(call.message, reg_name)

bot.polling()

