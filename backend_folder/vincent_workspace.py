import numpy as np
import pandas as pd
import IPython.display as ipt

# Beat tracking example
import librosa

# 1. Get the file path
filename = '../audio/sample3.WAV'

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename, sr=60)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Frequency
freq = librosa.stft(y)

# Intensity
db = librosa.amplitude_to_db(freq)