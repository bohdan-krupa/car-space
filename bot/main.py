import telebot
import time
from flask import Flask, request
from messages import *
from config import IS_DEPLOYED, TOKEN, WEBHOOK_URL, WEBHOOK_SECRET, OPENCAGE_KEY
from sql_worker import SQL
from parking_coords import ParkingCoords
from opencage.geocoder import OpenCageGeocode


bot = telebot.TeleBot(TOKEN, threaded=False)
geocoder = OpenCageGeocode(OPENCAGE_KEY)

@bot.message_handler(commands=['start'])
def welcome(msg):
  bot.send_message(msg.chat.id, HELLO)


@bot.message_handler(content_types=["location"])
def send_parking_by_geo(msg):
  try:
    send_parking(msg.chat.id, msg.location.latitude, msg.location.longitude)
  except Exception as e:
    print(e)


@bot.message_handler(content_types=["text"])
def send_parking_by_address(msg):
  try:
    result = geocoder.geocode(f'{msg.text}, Lviv', no_annotations=1, language='ua')
    lat = result[0]['geometry']['lat']
    lon = result[0]['geometry']['lng']

    send_parking(msg.chat.id, lat, lon)
  except Exception as e:
    print(e)


def send_parking(chat_id, lat, lon):
  try:
    parkingCoords = ParkingCoords()
    parking = parkingCoords.getClosestParking(lat, lon)

    if (parking['is_camera']):
      bot.send_message(
        chat_id,
        f"Найближча парковка: {parking['street']}\nВільні місця: {parking['spaces_amount']}"
      )
      photo = open(f"recognition/images/{parking['street']}.jpg", 'rb')
      bot.send_photo(chat_id, photo)
    else:
      bot.send_message(
        chat_id,
        f"Найближча парковка: {parking['street']}\nНа даній парковці поки немає камери"
      )
      
    bot.send_location(chat_id, parking['lat'], parking['lon'])
  except Exception as e:
    print(e)


if __name__ == '__main__':
  if IS_DEPLOYED:
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url=WEBHOOK_URL + WEBHOOK_SECRET)

    app = Flask(__name__)

    @app.route('/' + WEBHOOK_SECRET, methods=['POST'])
    def webhook():
      bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
      return 'ok', 200
      
    app.run()
  else:
    bot.remove_webhook()
    bot.polling(none_stop=True)