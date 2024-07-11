import openai
import requests
from domain.audio_repository import TranscribeRepository
from domain.chat_repository import ChatRepository
import os

class OpenAIAPI(TranscribeRepository, ChatRepository):
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def transcribe_audio(self, filename):
        print("Transcribing audio...")
        audio_file= open(filename, "rb")
        response = openai.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
        )
        transcription = response.text

        print("Transcribing finished...")
        return transcription

    def chat_with_gpt(self, transcription):
        print("Chatting with GPT...")
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": transcription}
                    ],
                }
            ],
        )

        print("Chatting finished...")
        return response.choices[0].message.content
