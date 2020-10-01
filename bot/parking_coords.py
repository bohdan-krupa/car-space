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
      'lon': parking[4],
      'is_camera': parking[5]
    }, parkings))


  def distance(self, lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))


  def get_sorted_by_distance(self, data, v):

    parkings_with_distances = list(
      map(lambda p: [
        self.distance(v['lat'], v['lon'], p['lat'], p['lon']),
        p
      ], data)
    )
    sorted_parkings = sorted(parkings_with_distances, key=lambda p: p[0])

    return sorted_parkings


  def get_5_closest_parking(self, lat, lon):
    first_5 = self.get_sorted_by_distance(self.parkings, {'lat': lat, 'lon': lon})[:5]
    parkings = list(map(lambda p: p[1], first_5))

    return parkings