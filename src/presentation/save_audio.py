from application.audio_service import AudioService

def save_audio(audio_data, sample_rate, filename):
    audio_service = AudioService()
    audio_service.save_audio(audio_data, sample_rate, filename)
