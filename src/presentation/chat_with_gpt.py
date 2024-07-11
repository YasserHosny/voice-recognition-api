from application.chat_service import ChatService

def chat_with_gpt(transcription):
    chat_service = ChatService()
    response = chat_service.chat_with_gpt(transcription)
    return response
