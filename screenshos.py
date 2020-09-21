import time
from cv2 import cv2

vidcap = cv2.VideoCapture('http://194.44.209.238/mjpg/video.mjpg')
success, image = vidcap.read()

while success:
  cv2.imwrite('input.jpg', image)    
  success, image = vidcap.read()
  print('Read a new frame: ', success)
  time.sleep(10)