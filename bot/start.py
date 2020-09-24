from bot_info import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(msg):
    bot.send_message(msg.chat.id, "Hello")


@bot.message_handler(commands=['location'])
def send_location(msg):
    bot.send_location(msg.chat.id, 49.8625278, 24.0177351)





if __name__ == '__main__':
    bot.polling()
    