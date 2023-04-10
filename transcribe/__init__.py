import os
import openai
from pydub import AudioSegment


def transcribe(ogg_file_path: str, mp3_file_path: str):
    try:
        AudioSegment.from_ogg(ogg_file_path).export(mp3_file_path, format="mp3")

        audio_file = open(mp3_file_path, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file, api_key=os.getenv("OPENAI_API_KEY"))

        text_file_path = ogg_file_path.replace(".ogg", ".txt")

        with open(text_file_path, "w") as f:
            f.write(transcript.text)
    except Exception as e:
        print(e)
    finally:
        if os.path.exists(mp3_file_path):
            os.remove(mp3_file_path)
