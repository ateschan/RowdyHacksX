import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import IPython.display as ipt

# Beat tracking example
import librosa

# 1. Get the file path
filename = '../audio/sample3.WAV'

samples, sample_rate = librosa.load(filename, sr=100000)
total_samples = len(samples)
duration = total_samples / sample_rate

print("Samples array: ", samples)
print("Total number of samples: ", total_samples)
print("Samples per second: ", sample_rate)
print("Audio duration: ", duration)

freq = librosa.stft(samples, n_fft=sample_rate//15)

pd.Series(samples).plot(figsize=(10,5), lw=1, title='STFT')

plt.show()