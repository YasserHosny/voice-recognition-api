from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from application.audio_service import AudioService
from application.chat_service import ChatService

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

audio_service = AudioService()
chat_service = ChatService()

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    transcription = audio_service.transcribe_audio(filepath)
    response = chat_service.chat_with_gpt(transcription)
    return jsonify({"transcription": transcription, "response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
