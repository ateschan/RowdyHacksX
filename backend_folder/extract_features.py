import librosa as lb
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from numpy.ma.core import argsort
from scipy.signal import find_peaks
from sklearn.preprocessing import MinMaxScaler
from matplotlib.ticker import ScalarFormatter

sample_rate = 44100
# load audio file
audio, sr = lb.load("../audio/Dream-Remix.mp3", sr=sample_rate)

# Amount of samples we dedicate to each frame which amount to 1/60 of a second
frame_size = sr//15

#outputs (frame_size/2)+1 frequency bins by (audioSamples - frame_size)/(frame_size/4) + 1
ft_audio = lb.stft(audio, n_fft=frame_size, hop_length=frame_size//4, win_length=frame_size//8)

# define important properties
number_of_freq_buckets = ft_audio.shape[0]
number_of_frames = ft_audio.shape[1]
audio_duration = lb.get_duration(y=audio, sr=sample_rate)
fps = number_of_frames/audio_duration

print(f"Frame_size for stft: {frame_size}\nRound file duration: {audio_duration}")
print(f"Frequency buckets: {number_of_freq_buckets}\nFrames of data: {number_of_frames}")
print(f"FPS: {fps}")

# Transpose fourier data into arrays of intensity per frequency bucket
ft_audio_t = np.transpose(ft_audio)
abs_audio = np.absolute(ft_audio_t)

# Frequency range covered by each bucket / division of data in fourier data array
freqs_per_bucket = (sample_rate//2)/number_of_freq_buckets

# NP array of frequency buckets to represent
frequency = np.linspace(0, sample_rate//2, frame_size//2+1)



# Transformer to normalize data from 0-1
min_max_scalar = MinMaxScaler(feature_range=(0,1))
freqs = []
normalized = []
# Minimum peak height to be considered
min_norm_height = 0.05

for frame in abs_audio:
    # normalize array of data
    norm = min_max_scalar.fit_transform(frame.reshape(-1, 1))
    normalized.append(norm.reshape(abs_audio[0].shape))
    # Set minimum height to filter freqs by
    min_height = min_norm_height
    # identify peak indexes
    peak_indexes,props = find_peaks(frame, distance=20, height=min_height)
    peak_heights = np.array(props['peak_heights'])

    # Turn indexes into respective frequencies
    peak_freqs = np.array((peak_indexes + 1) * freqs_per_bucket + (freqs_per_bucket // 2))

    # Sort peak_indexes in ascending order of peak heights
    peak_sort = peak_heights.argsort()
    # print(peak_heights)
    # print(peak_sort)
    # print(peak_freqs)
    sorted_peak_freqs = peak_freqs[peak_sort[::-1]]
    # print(sorted_peak_freqs)
    freqs.append(sorted_peak_freqs[:9])

f = np.array(freqs)
print(f.shape)
# plt.plot(frequency,normalized[2000])
# print(freqs[2000])
# for i in range(1000):
#     plt.plot(frequency, abs_audio[i+1000], "o", color="blue", markersize=1)
# plt.xscale('log')
# ax = plt.gca()
# # ax.set_xticks(frequency[1:])
# ax.xaxis.set_major_formatter(ScalarFormatter())

# print(freqs[0])

# sinwav = sin(2piFreqTr)



plt.show()









