import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("DEEPINFRA_TOKEN")
BASE_URL = "https://api.deepinfra.com/v1"

def create_voice(audio_path: str, name: str, description: str) -> str:
    url = f"{BASE_URL}/voices/add"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    with open(audio_path, "rb") as f:
        files = {
            "files": (Path(audio_path).name, f, "audio/mpeg")
        }
        data = {
            "name": name,
            "description": description
        }

        r = requests.post(url, headers=headers, files=files, data=data, timeout=120)

    print("STATUS:", r.status_code)
    print("BODY:", r.text)

    r.raise_for_status()
    return r.json()["voice_id"]

def synthesize(text: str, voice_id: str, out_file: str, language: str = "Italian"):
    url = f"{BASE_URL}/openai/audio/speech"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "Qwen/Qwen3-TTS",
        "input": text,
        "voice_id": voice_id,
        "language": language,
        "response_format": "mp3",
    }
    r = requests.post(url, headers=headers, json=payload, timeout=300)
    r.raise_for_status()
    Path(out_file).write_bytes(r.content)

if __name__ == "__main__":
    text = Path("Testo.txt").read_text(encoding="utf-8")

    # 1) crea voce custom da ref audio
    voice_id = create_voice(
        "audio_mp3_riferimento/LUCA_WARD_cut.mp3",
        name="Luca-Ward-clone",
        description="Attore italiano"
    )

    # 2) genera audio con quella voce
    synthesize(
        text=text,
        voice_id=voice_id,
        out_file="output_audio_mp3/output.mp3",
        language="Italian"
    )

    print("Audio salvato in output_audio_mp3/qwen3-luca-ward.mp3")