from abc import ABC, abstractmethod

class AudioRepository(ABC):
    @abstractmethod
    def record_audio(self, duration):
        pass

class AudioSaverRepository(ABC):
    @abstractmethod
    def save_audio(self, audio_data, sample_rate, filename):
        pass

class TranscribeRepository(ABC):
    @abstractmethod
    def transcribe_audio(self, filename):
        pass
