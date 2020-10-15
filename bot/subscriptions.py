import telebot
import time
from config import TOKEN
from sql_worker import SQL


bot = telebot.TeleBot(TOKEN, threaded=False)

while(True):
  database = SQL()
  subscriptions = database.get_subscriptions()
  subscriptions = list(map(lambda subscription: {
    'id': subscription[0],
    'user_id': subscription[1],
    'parking_id': subscriptions[2]
  }, subscriptions))

  for subscription in subscriptions:
    parking = database.get_parking()
    parking = {
      'id': parking[0],
      'street': parking[1],
      'spaces_amount': parking[2],
      'lat': float(parking[3]),
      'lon': float(parking[4]),
      'camera_url': parking[5]
    }

    if parking['spaces_amount'] <= 0:
      bot.send_message(subscription['user_id'], text=f"Парковка {parking['street']} вже зайнята")

  time.sleep(3)