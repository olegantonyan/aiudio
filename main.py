import output.pulseaudio as pulseaudio
import numpy as np

pa = pulseaudio.PulseAudio()
while True:
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 1.0   # in seconds, may be float
    f = 440.0        # sine frequency, Hz, may be float

    x = np.arange(sample)
    y = np.sin(2 * np.pi * f * x / Fs)

    pa.write(samples)
pa.free()
