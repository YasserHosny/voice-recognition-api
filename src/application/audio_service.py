from infrastructure.audio_recorder import AudioRecorder
from infrastructure.audio_saver import AudioSaver
from infrastructure.openai_api import OpenAIAPI

class AudioService:
    def __init__(self):
        self.audio_recorder = AudioRecorder()
        self.audio_saver = AudioSaver()
        self.transcriber = OpenAIAPI()

    def record_audio(self, duration):
        return self.audio_recorder.record_audio(duration)

    def save_audio(self, audio_data, sample_rate, filename):
        self.audio_saver.save_audio(audio_data, sample_rate, filename)

    def transcribe_audio(self, filename):
        return self.transcriber.transcribe_audio(filename)
