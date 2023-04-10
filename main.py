from dotenv import load_dotenv
from transcribe import transcribe

load_dotenv()

if __name__ == '__main__':
    ogg_file_path = "audios/WhatsApp Ptt 2023-04-10 at 11.26.02.ogg"
    mp3_file_path = ogg_file_path.replace(".ogg", ".mp3")
    transcribe(ogg_file_path, mp3_file_path)
