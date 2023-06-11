import time

import pyscreenshot as ImageGrab
import schedule

from datetime import datetime
from settings import path, screenshots_repeat


class Recorder:
    """Class from which other classes inherit"""
    def __init__(self, user_path):
        self.path = user_path

    def set_path(self, folder, format):
        name = f"{folder}/{str(datetime.now()).split('.')[0]}.{format}"
        return self.path + name

    @staticmethod
    def every_time(repeat, function):
        schedule.every(repeat).seconds.do(function)

        while True:
            try:
                schedule.run_pending()
            except Exception:
                pass
            time.sleep(1)


class Screenshots(Recorder):
    """Take a screenshot every n seconds"""
    def __init__(self):
        super().__init__(path)
        self.repeat = screenshots_repeat

    def take_screenshot(self):
        screenshot = ImageGrab.grab()
        screenshot.save(self.set_path('scrn', 'png'))

        return self.set_path('scrn', 'png')

    def run(self):
        self.every_time(self.repeat, self.take_screenshot)
