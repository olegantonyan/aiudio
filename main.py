import numpy as np

import output.pulseaudio as pulseaudio


def generate_sine_wave(f):
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 1.0   # in seconds, may be float
    x = np.arange(fs * duration)  # 1 full period
    y = (np.sin(2 * np.pi * f * x / fs) * 32768).astype(np.int16)
    samples = []
    for i in y:
        samples.append(i & 0xFF)
        samples.append(i >> 8 & 0xFF)
    return samples


pa = pulseaudio.PulseAudio()
try:
    data = generate_sine_wave(40)
    while True:
        pa.write(data)
finally:
    pa.free()
