from cv2 import cv2
import numpy as np

LAPLACIAN = 1.4

def apply(grayed, rect, coordinates, mask):
  roi_gray = grayed[rect[1]:(rect[1] + rect[3]), rect[0]:(rect[0] + rect[2])]
  laplacian = cv2.Laplacian(roi_gray, cv2.CV_64F)

  coordinates[:, 0] = coordinates[:, 0] - rect[0]
  coordinates[:, 1] = coordinates[:, 1] - rect[1]

  status = np.mean(np.abs(laplacian * mask)) < LAPLACIAN

  return status

image = cv2.imread('parking.png')
# blurred = cv2.GaussianBlur(image, (5, 5), 3)
# image = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

coordinates = np.array([[500, 400], [650, 425], [590, 470], [420, 425]])
# rect = cv2.boundingRect(coordinates)

# new_coordinates = coordinates.copy()
# new_coordinates[:, 0] = coordinates[:, 0] - rect[0]
# new_coordinates[:, 1] = coordinates[:, 1] - rect[1]

image = cv2.polylines(image, [coordinates], True, (0, 255, 0), thickness=2)

# mask = cv2.drawContours(
#   np.zeros((rect[3], rect[2]), dtype=np.uint8),
#   [new_coordinates],
#   contourIdx=-1,
#   color=255,
#   thickness=-1,
#   lineType=cv2.LINE_8)

# print(apply(image, rect, coordinates, mask))


cv2.imwrite('test.png', image)