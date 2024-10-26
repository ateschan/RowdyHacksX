import librosa

class AudioFrame:
    def __init__(self, frame_waveform):

        self.freq = librosa.stft(frame_waveform)
        self.intensity = librosa.amplitude_to_db(self.freq)
        self.offsets = ''