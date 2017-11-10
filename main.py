import output.pulseaudio as pulseaudio
import input.sine_wave as sine_wave
import input.file as file


pa = pulseaudio.PulseAudio()
try:
    for i in sine_wave.SineWave(440).generate():
        pa.write(i)
    #for i in file.File('/home/oleg/Desktop/output.wav').read():
    #    pa.write(i)
finally:
    pa.free()
