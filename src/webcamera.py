import cv2

from settings import (photo_width, photo_height,
                      camera_index, path, photo_repeat)
from src.screenshots import Recorder


class WebCamera(Recorder):
    """Take a photo from the webcam every n seconds"""

    def __init__(self):
        super().__init__(path)
        self.camera = cv2.VideoCapture(camera_index)
        self.width = photo_width
        self.height = photo_height
        self.repeat = photo_repeat

    def take_photo(self):
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.height)

        _, image = self.camera.read()
        cv2.imwrite(self.set_path('wbc', 'png'), image)
        self.camera.release()

    def run(self):
        self.every_time(self.repeat, self.take_photo)
