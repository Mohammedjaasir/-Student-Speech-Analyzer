import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    transcript = result["text"]
    duration = result["segments"][-1]["end"]
    return transcript, duration
