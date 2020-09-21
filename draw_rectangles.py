import numpy as np
from cv2 import cv2
from shapely.geometry import Polygon

def loltlot(list_of_list): # list of lists to list of tuples
  return list(map(tuple, list_of_list))

image = cv2.imread('input.jpg')

color = (0, 255, 0)
thickness = 2

pts_array = [
  np.array([[200, 66], [248, 66], [248, 98], [200, 98]], np.int32),
  np.array([[400, 66], [48, 100], [150, 300]], np.int32),
  np.array([[330, 340], [370, 335], [380, 365], [340, 370]], np.int32)
]


p1 = Polygon(loltlot(pts_array[0]))
p2 = Polygon(loltlot(pts_array[1]))
print(p1.intersects(p2))


image = cv2.polylines(image, pts_array, True, color, thickness)
cv2.imwrite('drawed_result.jpg', image)