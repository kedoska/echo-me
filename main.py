import os
import sys

from dotenv import load_dotenv
from transcribe import transcribe, convert_ogg_to_mp3, openai_transcribe

load_dotenv()

if __name__ == '__main__':

    if len(sys.argv) < 2:
        raise Exception("Please provide an ogg file path.")

    ogg_file_path = sys.argv[1]

    if not os.path.exists(ogg_file_path):
        raise Exception(f"File {ogg_file_path} does not exist.")

    mp3_file_path = ogg_file_path.replace(".ogg", ".mp3")
    convert_ogg_to_mp3(ogg_file_path, mp3_file_path)

    text_file_path = ogg_file_path.replace(".ogg", ".txt")

    transcribe(mp3_file_path, text_file_path, transcribe_driver=openai_transcribe)

