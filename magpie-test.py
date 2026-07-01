from pathlib import Path
from datetime import datetime
import shutil
from gradio_client import Client

INPUT_FILE = Path("Testo.txt")
OUTPUT_DIR = Path("output_audio_mp3")

client = Client("nvidia/magpie_tts_multilingual_demo")

text = INPUT_FILE.read_text(encoding="utf-8")

result = client.predict(
    input_text=text,
    language="it",
    speaker="Jason",
    apply_TN="Do not apply TN",
    api_name="/demo_tts",
)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

src = Path(result)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
dst = OUTPUT_DIR / f"{INPUT_FILE.stem}_{timestamp}{src.suffix}"

shutil.copy2(src, dst)

print(f"Audio salvato in: {dst}")