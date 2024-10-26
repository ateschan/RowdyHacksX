import librosa

class AudioFile:
    def __init__(self, filepath):
        # Load the audio file in the notebook as a wavefor and store the sample rate
        audio_data, self.sample_rate = librosa.load(filepath)
        
        # Get the estimated tempo of the track
        self.tempo, beat_frames = librosa.beat.beat_track(y=audio_data, sr=self.sample_rate)
        
        # Convert the beat frames into timings
        self.beat_times = librosa.frames_to_time(beat_frames, sr=self.sample_rate)
        
        # Audio duration
        self.duaration = librosa.get_duration(y=audio_data, sr=self.sample_rate)
        
        # Frames
        self.frames = []
        
sample = AudioFile('../../audio/sample3.WAV')
print(sample.duaration)