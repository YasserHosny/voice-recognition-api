import wave
from domain.audio_repository import AudioSaverRepository

class AudioSaver(AudioSaverRepository):
    def save_audio(self, audio_data, sample_rate, filename):
        with wave.open(filename, 'w') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes(audio_data.tobytes())
