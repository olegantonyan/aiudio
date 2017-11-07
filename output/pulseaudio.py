import ctypes
import sys


class PulseAudioError(RuntimeError):
    pass


class PulseAudio:
    class struct_pa_sample_spec(ctypes.Structure):
        __slots__ = ['format', 'rate', 'channels']

    struct_pa_sample_spec._fields_ = [
        ('format', ctypes.c_int),
        ('rate', ctypes.c_uint32),
        ('channels', ctypes.c_uint8),
    ]

    # pa_sample_spec = struct_pa_sample_spec

    def __init__(self):
        self._libpulse = ctypes.cdll.LoadLibrary('libpulse-simple.so.0')

        sample_spec = self.struct_pa_sample_spec()
        sample_spec.rate = 44100
        sample_spec.channels = 1
        sample_spec.format = 3  # PA_SAMPLE_S16LE

        error = ctypes.c_int(0)
        self._stream = self._libpulse.pa_simple_new(
            None,  # Default server.
            'aiudio pulse',  # Application's name.
            1,  # Stream for playback. PA_STREAM_PLAYBACK
            None,  # Default device.
            'playback',  # Stream's description.
            ctypes.byref(sample_spec),  # Sample format.
            None,  # Default channel map.
            None,  # Default buffering attributes.
            ctypes.byref(error)  # Ignore error code.
        )
        if not self._stream:
            raise PulseAudioError('could not create pulseaudio stream: {0}'.format(self._libpulse.strerror(ctypes.byref(error))))

    def write(self, sample):
        error = ctypes.c_int(0)
        if self._libpulse.pa_simple_write(self._stream, bytes(sample), len(sample), error):
            raise PulseAudioError('could not write pulseaudio stream')

    def free(self):
        error = ctypes.c_int(0)
        if self._libpulse.pa_simple_drain(self._stream, ctypes.byref(error)):
            raise PulseAudioError('could not simple drain')
        self._libpulse.pa_simple_free(self._stream)
