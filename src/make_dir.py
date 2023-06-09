import os
from settings import path

def make_dir():
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(path + "Screenshots"):
        os.mkdir(path + "Screenshots")
    if not os.path.exists(path + "Microphone"):
        os.mkdir(path + "Microphone")
    if not os.path.exists(path + 'WebCamera'):
        os.mkdir(path + 'WebCamera')

def run():
    make_dir()
