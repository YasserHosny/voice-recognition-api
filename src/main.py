from presentation.record_audio import record_audio
from presentation.save_audio import save_audio
from presentation.transcribe_audio import transcribe_audio
from presentation.chat_with_gpt import chat_with_gpt
import os

def main():
    duration = 5  # seconds
    sample_rate = 16000
    audio_filename = 'audio.wav'

    #check file exists
    if not os.path.isfile(audio_filename):
        audio_data = record_audio(duration)
        save_audio(audio_data, sample_rate, audio_filename)

    transcription = transcribe_audio(audio_filename)
    print(f"Transcription: {transcription}")

    response = chat_with_gpt(transcription)
    print(f"ChatGPT response: {response}")

if __name__ == "__main__":
    main()
