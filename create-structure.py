import os

# Define the structure
structure = {
    "src": {
        "presentation": [
            "record_audio.py",
            "save_audio.py",
            "transcribe_audio.py",
            "chat_with_gpt.py"
        ],
        "application": [
            "audio_service.py",
            "chat_service.py"
        ],
        "domain": [
            "audio_repository.py",
            "chat_repository.py"
        ],
        "infrastructure": [
            "openai_api.py",
            "audio_recorder.py",
            "audio_saver.py"
        ]
    }
}

# Function to create directories and files
def create_structure(base_path, structure):
    for folder, content in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        
        if isinstance(content, dict):
            create_structure(folder_path, content)
        elif isinstance(content, list):
            for file in content:
                file_path = os.path.join(folder_path, file)
                with open(file_path, 'w') as f:
                    pass



# Create the structure
base_path = "."
create_structure(base_path, structure)

print("Folder and file structure created successfully.")
