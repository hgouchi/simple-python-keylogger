import time
import sounddevice as sd

import schedule
from scipy.io.wavfile import write

from datetime import datetime
from settings import path, microphone_time, microphone_repeat


class Microphone:
    """Record microphone every n seconds"""
    audio_name = f"audio-{str(datetime.now()).split('.')[0]}.wav"
    path = path = path + 'Microphone/' + audio_name

    def __init__(self):
        self.fq = 44100
        self.seconds = microphone_time

    def record_micro(self):
        recording = sd.rec(self.seconds * self.fq, samplerate=self.fq, channels=2)
        sd.wait()

        write(path + 'Microphone/' + self.audio_name, self.fq, recording)

    def every_time(self):
        schedule.every(microphone_repeat).seconds.do(self.record_micro)

        while True:
            try:
                schedule.run_pending()
            except Exception:
                pass
            time.sleep(1)
