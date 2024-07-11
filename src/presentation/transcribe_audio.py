from application.audio_service import AudioService

def transcribe_audio(filename):
    audio_service = AudioService()
    transcription = audio_service.transcribe_audio(filename)
    return transcription
