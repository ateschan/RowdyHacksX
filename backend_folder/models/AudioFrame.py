import numpy as np
import librosa

# 60 FPS
class AudioFrame:
    def __init__(self, frame_waveform):

        self.freq = np.fft.fft(frame_waveform)
        self.intensity = librosa.amplitude_to_db(self.freq)
        self.offsets = ''