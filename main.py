import os
import sys

from dotenv import load_dotenv
from transcribe import transcribe

load_dotenv()

if __name__ == '__main__':

    if len(sys.argv) < 2:
        raise Exception("Please provide an ogg file path.")

    ogg_file_path = sys.argv[1]

    if not os.path.exists(ogg_file_path):
        raise Exception(f"File {ogg_file_path} does not exist.")

    mp3_file_path = ogg_file_path.replace(".ogg", ".mp3")
    transcribe(ogg_file_path, mp3_file_path)
