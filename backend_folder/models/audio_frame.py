import math

import numpy as np
import librosa

# 60 FPS
class AudioFrame:
    data = []
    def __init__(self, freqs, amps, sample_rate: int):

        self.sample_bins = np.linspace(0, np.pi,512)

        for i in range(len(amps)):
            d = [self.sine(amps[i], freqs[i], self.sample_bins[x]) for x in range(len(self.sample_bins))]
            self.data.append(d)


    def sine(self, amp, freq, time, offset=0):

        data = amp*np.sin(2*np.pi*freq*time)
        return data