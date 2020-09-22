import argparse
from cv2 import cv2 as open_cv
import time
import yaml
from motion_detector import MotionDetector
from colors import *
import logging


def main():
    logging.basicConfig(level=logging.INFO)

    args = parse_args()

    data_file = args.data_file
    start_frame = args.start_frame
    without_id = 'http://vs7.videoprobki.com.ua/streams/cam673stream_'
    url = findCurrentMinute(without_id)
    photoId = 1

    with open(data_file, "r") as data:
        points = yaml.load(data)
        while True:
            detector = MotionDetector(url, points, int(start_frame))
            start_time = time.time()
            detector.detect_motion(photoId)
            exec_time = time.time() - start_time
            photoId = photoId + 1
            time.sleep(60 - exec_time)
            url = nextUrl(url)
            print(url)

def findCurrentMinute(without_id):
    current_timestamp = round(time.time())
    while True:
        if (open_cv.VideoCapture(without_id + str(current_timestamp) + '.mp4').isOpened()):
            return without_id + str(current_timestamp) + '.mp4'
        current_timestamp = current_timestamp - 1


def nextUrl(currentUrl):
    id = int(currentUrl.split('_')[1].split('.')[0]) + 62
    without_id = currentUrl.split('_')[0]
    if (open_cv.VideoCapture(without_id + "_" + str(id) + '.mp4').isOpened()):
        print("Default")
        return without_id + "_" + str(id) + '.mp4'
    elif (open_cv.VideoCapture(without_id + "_" + str(id - 1) + '.mp4').isOpened()):
        print("-1")
        return without_id + "_" + str(id - 1) + '.mp4'
    else:
        print("+1")
        return without_id + "_" + str(id + 1) + '.mp4'

def parse_args():
    parser = argparse.ArgumentParser(description='Start recognition')

    parser.add_argument("--data",
                        dest="data_file",
                        required=True,
                        help="Data file to be used with OpenCV")

    parser.add_argument("--start-frame",
                        dest="start_frame",
                        required=False,
                        default=1,
                        help="Starting frame on the video")

    return parser.parse_args()


if __name__ == '__main__':
    main()