from infrastructure.openai_api import OpenAIAPI

class ChatService:
    def __init__(self):
        self.openai_api = OpenAIAPI()

    def chat_with_gpt(self, transcription):
        return self.openai_api.chat_with_gpt(transcription)
