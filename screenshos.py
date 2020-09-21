import time
from cv2 import cv2
from recognition import recognite_cars

vidcap = cv2.VideoCapture('http://194.44.209.238/mjpg/video.mjpg')
success, image = vidcap.read()

while success:
  cv2.imwrite('input1.jpg', image)
  print('Writed new snapshot')

  recognite_cars(parking_id=1)
  print('Recognited new snapshot')

  success, image = vidcap.read()
  # time.sleep(10)