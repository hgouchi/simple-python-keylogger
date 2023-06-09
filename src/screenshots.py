#!/usr/bin/python3

import time

import pyscreenshot as ImageGrab
import schedule

from datetime import datetime
from settings import path, screenshots_repeat


class Screenshots:
    """Take a screenshot every n seconds"""
    image_name = f"screenshot-{str(datetime.now()).split('.')[0]}.png"
    path = path + 'Screenshots/' + image_name

    @classmethod
    def take_screenshot(cls):
        screenshot = ImageGrab.grab()
        screenshot.save(cls.path)

        return cls.path

    def every_time(self):
        schedule.every(screenshots_repeat).seconds.do(self.take_screenshot)

        while True:
            try:
                schedule.run_pending()
            except Exception:
                pass
            time.sleep(1)
