import librosa as lb
import numpy as np
from scipy.signal import find_peaks
from sklearn.preprocessing import MinMaxScaler
from .audio_frame import AudioFrame



class AudioFile:
    frames: list  = []

    def __init__(self, filepath, sample_rate=44100):
        self.sample_rate = sample_rate

        self.samples, _= lb.load(filepath, sr=sample_rate)

        self.duration = lb.get_duration(y=self.samples, sr=self.sample_rate)

        # Perform fft and populate data
        self.freqs, self.amplitudes = self.get_fft()


        for i in range(len(self.freqs)):
            self.frames.append(AudioFrame(self.freqs[i], self.amplitudes[i], sample_rate=self.sample_rate))
        
    def get_fft(self):
        print("Perform fft")
        frame_size = self.sample_rate//15
        # Perform discrete fourier transform
        ft_audio = lb.stft(self.samples, n_fft=frame_size, hop_length=frame_size // 4, win_length=frame_size // 8)

        # define important properties
        number_of_freq_buckets = ft_audio.shape[0]
        number_of_frames = ft_audio.shape[1]
        audio_duration = lb.get_duration(y=self.samples, sr=self.sample_rate)
        fps = number_of_frames / audio_duration

        print("Fourier Transform attributes:")
        print(f"\tFrame_size for stft: {frame_size}\n\tRound file duration: {audio_duration}")
        print(f"\tFrequency buckets: {number_of_freq_buckets}\n\tFrames of data: {number_of_frames}")
        print(f"\tFPS: {fps}")

        # Transpose fourier data into arrays of intensity per frequency bucket
        ft_audio_t = np.transpose(ft_audio)
        abs_audio = np.absolute(ft_audio_t)

        # Frequency range covered by each bucket / division of data in fourier data array
        freqs_per_bucket = (self.sample_rate // 2) / number_of_freq_buckets

        # NP array of frequency buckets to represent
        frequency = np.linspace(0, self.sample_rate // 2, frame_size // 2 + 1)

        # Transformer to normalize data from 0-1
        min_max_scalar = MinMaxScaler(feature_range=(0, 1))
        # Hold freq and freq amplitudes sorted
        freqs = []
        amps = []
        # Minimum peak height to be considered
        min_norm_height = 0.05

        # Normalize and get top 9 frequencies per frame
        for frame in abs_audio:
            # normalize array of data
            norm_data = min_max_scalar.fit_transform(frame.reshape(-1, 1))

            # TODO: Set minimum height to filter freqs by
            min_height = min_norm_height

            # identify peak indexes
            peak_indexes, props = find_peaks(frame, distance=20, height=min_height)
            peak_heights = np.array(props['peak_heights'])

            # Turn indexes into respective frequencies
            peak_freqs = np.array((peak_indexes + 1) * freqs_per_bucket + (freqs_per_bucket // 2))

            # Sort peak_indexes and height data in ascending order of peak heights
            peak_sort = peak_heights.argsort()
            sorted_peak_freqs = peak_freqs[peak_sort[::-1]]
            sorted_peak_heights = peak_heights[peak_sort[::-1]]

            # Add frame freqs and amplitudes to arrays
            freqs.append(np.array(sorted_peak_freqs[:9]))
            amps.append(np.array(sorted_peak_heights[:9]))


        return freqs, amps


    def get_rhythm(self):
        pass
