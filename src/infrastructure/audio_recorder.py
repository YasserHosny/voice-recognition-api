import sounddevice as sd
from domain.audio_repository import AudioRepository

class AudioRecorder(AudioRepository):
    def record_audio(self, duration, sample_rate=16000):
        print("Recording...")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        print("Recording finished.")
        return audio_data
