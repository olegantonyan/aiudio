import output.pulseaudio as pulseaudio
import numpy as np

pa = pulseaudio.PulseAudio()
while True:
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 10.0   # in seconds, may be float
    f = 440.0        # sine frequency, Hz, may be float

    x = np.arange(fs * duration)  # 1 full period
    y = (np.sin(2 * np.pi * f * x / fs) * 32768).astype(np.int16)
    samples = []
    for i in y:
        samples.append(i & 0xFF)
        samples.append(i >> 8 & 0xFF)

    pa.write(bytes(samples))
pa.free()
