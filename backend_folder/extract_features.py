import librosa as lb
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import find_peaks

sample_rate = 44100
# load audio file
audio, sr = lb.load("../audio/piano.wav", sr=sample_rate)

# Amount of samples we dedicate to each frame which amount to 1/60 of a second
frame_size = 2048
print(f"Frame_size for stft: {frame_size}")

#outputs (frame_size/2)+1 frequency bins by (audioSamples - frame_size)/(frame_size/4) + 1
ft_audio = lb.stft(audio, n_fft=frame_size, hop_length=frame_size//16, win_length=frame_size//4)
print(ft_audio.shape)
number_of_freq_buckets = ft_audio.shape[0]
number_of_frames = ft_audio.shape[1]
print(f"# Frequency buckets: {number_of_freq_buckets}\n# Frames of data: {number_of_frames}")
print(f"ft_audio[0] length: {len(ft_audio[0])}")
ft_audio_t = np.transpose(ft_audio)
abs_audio = np.absolute(ft_audio_t)
# freq_of_bucket = (bucket_index + 1) * freq_per_buc + (freq_per_buc/2)

frequency = np.linspace(0, sample_rate//2, frame_size//2+1)
plt.plot(frequency,abs_audio[4])
plt.plot(frequency,abs_audio[1])
plt.plot(frequency,abs_audio[200])
plt.plot(frequency,abs_audio[50])
plt.show()


freqs = []
freqs_per_bucket = (sample_rate//2)/number_of_freq_buckets
for frame in abs_audio:
    peak_indexes,_ = find_peaks(frame, distance=10)
    freqs = frame[peak_indexes]
    freqs
print(freqs)









