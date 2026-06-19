import base64
import os
from pathlib import Path
from dotenv import load_dotenv
from mistralai.client import Mistral

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)

# 1. Leggere testo da file.txt
text = Path("Testo.txt").read_text(encoding="utf-8")

# 2. File audio di riferimento
audio_path = "audio_mp3_riferimento/LUCA_WARD.mp3"
ref_audio_b64 = base64.b64encode(Path(audio_path).read_bytes()).decode()

# 3. Genera audio
audio = client.audio.speech.complete(
    model="voxtral-mini-tts-2603",
    input=text,
    response_format="mp3",
    stream=False,
    ref_audio=ref_audio_b64,
)

# 4. Salva
Path("output_audio_mp3/output_luca_ward.mp3").write_bytes(base64.b64decode(audio.audio_data))

print("Audio salvato in output_luca_ward.mp3")