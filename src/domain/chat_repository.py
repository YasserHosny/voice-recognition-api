from abc import ABC, abstractmethod

class ChatRepository(ABC):
    @abstractmethod
    def chat_with_gpt(self, transcription):
        pass
