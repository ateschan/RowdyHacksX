from models.audio_file import AudioFile
from models.audio_frame import AudioFrame
import matplotlib.pyplot as plt

file = AudioFile("../audio/sample1.WAV")
plt.figure(figsize=(16, 10))
frame: AudioFrame = file.frames[70]
print(frame.data)
for fr in frame.data:
    plt.plot(frame.sample_bins, fr)
plt.show()