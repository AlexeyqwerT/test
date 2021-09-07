import telebot
from telebot import types
name ='';
surname ='';
age =0;

bot = telebot.TeleBot("1932464805:AAFLOJym4MJkD71-PjZiiYDreKex3gI9xxk")

@bot.message_handler(content_types=["text"])

def otvet(message):
  if message.text.lower()== 'привет':


    bot.send_message (message.chat.id,"ДАРОВА")
  elif message.text.lower()=='как дела':
    bot.send_message(message.chat.id,"Нормально,а у вас?")
  elif message.text =='/help':
    bot.send_message(message.chat.id,"/reg-регистрация")
  elif message.text =='/reg':
    bot.send_message(message.chat.id,"Как тебя зовут?")
    bot.register_next_step_handler(message,information)
  elif message.text =='/info':
    bot.send_message(message.chat.id,info)
  else:
    bot.send_message (message.chat.id,"Я не понимаю тебя.Напиши /help чтобы увидеть список команд!")
def information(message):
  global name;
  name=message.text
  bot.send_message(message.chat.id,"Что насчёт твоей фамилии?")
  bot.register_next_step_handler(message,get_surname)
def get_surname(message):
  global surname
  surname =message.text;
  bot.send_message(message.chat.id,"Твой возраст?")
  bot.register_next_step_handler(message,get_age)
def get_age(message):
  global age
  while age==0:
    try:
      age=int(message.text)
    except Exception:
      bot.send_message(message.chat.id,"Циферками")




  keyboard = types.InlineKeyboardMarkup()
  key_yes =types.InlineKeyboardButton(text="Да",callback_data="yes")
  keyboard.add(key_yes)
  key_no =types.InlineKeyboardButton(text="Нет",callback_data="no")
  keyboard.add(key_no)
  question=('Тебе ' + str(age) + ' лет,тебя зовут ' + name + ' ' + surname + '?')
  bot.send_message(message.chat.id,text=question,reply_markup=keyboard)
@bot.callback_query_handler(func=lambda cal:True)
def callback_worker(call):
  if call.data=="yes":
    bot.send_message(call.message.chat.id,"Попытаюсь запомнить!")
    global info;
    info = f'{surname} {name} {age}'
  else:
    bot.send_message(call.message.chat.id,"Я не продуманный бот.Регайся занаво!")




bot.polling(none_stop=True,interval=0)
