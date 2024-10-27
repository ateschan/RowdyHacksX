import math

import numpy as np
import librosa

# 60 FPS
class AudioFrame:
    # static array data = []

    def __init__(self, freqs, amps, sample_rate: int):

        self.sample_bins = np.linspace(0, np.pi,512)
        self.freqs = freqs # top 9 freqs
        self.amps = amps # up to top 9 heights

        data = []
        for i in range(len(freqs)):
            d = []
            for point in self.sample_bins:
                d.append(self.sine(amps[i], freqs[i], point))
            data.append(d)
        self.data = data
        print(f"Data length: {len(self.data)}")

    def sine(self, amp, freq, time, offset=0):
        return amp*np.sin(2*np.pi*freq*time)