from math import cos, asin, sqrt
from sql_worker import SQL

class ParkingCoords:
  def __init__(self):
    database = SQL()
    parkings = database.get_all_parkings()

    self.parkings = list(map(lambda parking: {
      'id': parking[0],
      'street': parking[1],
      'spaces_amount': parking[2],
      'lat': parking[3],
      'lon': parking[4]
    }, parkings))


  def distance(self, lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))


  def closest(self, data, v):
    return min(data, key=lambda p: self.distance(v['lat'], v['lon'], p['lat'], p['lon']))


  def getClosestParking(self, lat, lon):
    return self.closest(self.parkings, {'lat': lat, 'lon': lon})