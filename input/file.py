import wave


class File:
    def __init__(self, path):
        self._path = path

    def read(self, chunk_size=1024):
        wf = wave.open(self._path, 'rb')
        while True:
            buf = wf.readframes(chunk_size)
            if buf == '':
                break

            samples = []
            prev = 0
            for idx, value in enumerate(buf):
                if idx % 2 == 1:
                    samples.append(value << 8 | prev)
                prev = value

            yield(samples)
            del samples[:]

        wf.close()
