import sounddevice as sd
from scipy.io.wavfile import write

from settings import path, microphone_time, microphone_repeat
from src.screenshots import Recorder


class Microphone(Recorder):
    """Record microphone every n seconds"""

    def __init__(self):
        super().__init__(path)
        self.fq = 44100
        self.seconds = microphone_time
        self.repeat = microphone_repeat

    def record_micro(self):
        recording = sd.rec(self.seconds * self.fq,
                           samplerate=self.fq, channels=2)
        sd.wait()

        write(self.set_path('mcrn', 'wav'), self.fq, recording)

    def run(self):
        self.every_time(self.repeat, self.record_micro)
