from application.audio_service import AudioService

def record_audio(duration):
    audio_service = AudioService()
    audio_data = audio_service.record_audio(duration)
    return audio_data
