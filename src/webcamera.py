import time

import cv2
import schedule

from datetime import datetime
from settings import (photo_width, photo_height,
                      camera_index, path, photo_repeat)


class WebCamera:
    """Take a photo from the webcam every n seconds"""
    photo_name = f"photo-{str(datetime.now()).split('.')[0]}.png"

    def __init__(self):
        self.camera = cv2.VideoCapture(camera_index)
        self.path = path + 'WebCamera/' + self.photo_name

    def take_photo(self):
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, photo_width)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, photo_height)

        _, image = self.camera.read()
        cv2.imwrite(self.path, image)
        self.camera.release()

    def every_time(self):
        schedule.every(photo_repeat).seconds.do(self.take_photo)

        while True:
            try:
                schedule.run_pending()
            except Exception:
                pass
            time.sleep(1)
