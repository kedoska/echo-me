import os
import openai
from pydub import AudioSegment


def openai_transcribe(mp3_file_path: str) -> str:
    try:
        audio_file = open(mp3_file_path, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file, api_key=os.getenv("OPENAI_API_KEY"))
        return transcript.text
    except Exception as e:
        print(e)


def convert_ogg_to_mp3(ogg_file_path: str, mp3_file_path: str):
    try:
        print(f"Converting {ogg_file_path} to {mp3_file_path}...")
        AudioSegment.from_ogg(ogg_file_path).export(mp3_file_path, format="mp3")
    except Exception as e:
        print(e)


def transcribe(mp3_file_path: str, text_file_path: str, transcribe_driver=openai_transcribe):
    try:
        print(f"Transcribing {mp3_file_path} to {text_file_path}...")
        text = transcribe_driver(mp3_file_path)

        with open(text_file_path, "w") as f:
            f.write(text)
    except Exception as e:
        print(e)
    finally:
        if os.path.exists(mp3_file_path):
            os.remove(mp3_file_path)
