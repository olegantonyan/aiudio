import numpy as np


class SineWave:
    def __init__(self, frequency, sample_rate=44100, channels=2):
        self._x = np.arange(sample_rate)
        self._y = (np.sin(2 * np.pi * frequency * self._x / sample_rate) * 32768).astype(np.int16)
        self._channels = channels

    def generate(self, chunk_size=1024):
        result = []
        counter = 0
        while True:
            for i in self._y:
                result.append(i)
                if self._channels == 2:
                    result.append(i)
                counter += 1
                if counter == chunk_size:
                    yield(result)
                    del result[:]
                    counter = 0
