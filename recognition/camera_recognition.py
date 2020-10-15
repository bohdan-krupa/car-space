import argparse
import os
import sys
import requests as req
from cv2 import cv2 as open_cv
import time
import yaml
from motion_detector import MotionDetector
from sql_worker import SQL as Database

def main():
    args = parse_args()

    street_name = args.name
    camera_link = args.camera
    current_frame = findCurrentMinute(camera_link)

    db = Database()

    with open("recognition/data/" + street_name + ".yml", "r") as data:
        points = yaml.load(data)
        while True:
            if current_frame is not None:
                detector = MotionDetector(points)
                start_time = time.time()
                space_amount = detector.detect_motion(street_name, current_frame)
                db.set_spaces_amount(1, space_amount)
                exec_time = time.time() - start_time
                time.sleep(63 - exec_time)

            current_frame = findCurrentMinute(camera_link)

def findCurrentMinute(without_id):
    current_timestamp = round(time.time())
    while True:
        if (req.get(without_id + str(current_timestamp) + '.mp4').status_code != 404):
            # print("Opened")
            return_url = without_id + str(current_timestamp) + '.mp4'
            print(return_url)
            return getFrame(return_url)
        # print("Aint found")
        current_timestamp = current_timestamp - 1

def getFrame(url):
    capture = open_cv.VideoCapture(url)
    frameAmount = int(capture.get(open_cv.CAP_PROP_FRAME_COUNT))
    capture.set(open_cv.CAP_PROP_POS_FRAMES, frameAmount / 2)

    if capture.isOpened():
        # print("IsOpened")
        result, frame = capture.read()
        if frame is None:
            # print("How?")
            return None

        if not result:
            return None

        return frame
    else:
        # print("IsNotOpened")
        return None


def parse_args():
    parser = argparse.ArgumentParser(description='Start recognition')

    parser.add_argument("--name",
                        dest="name",
                        required=True,
                        help="Name of street")

    parser.add_argument("--camera",
                        dest="camera",
                        required=True,
                        help="Link to camera")

    return parser.parse_args()


if __name__ == '__main__':
    main()