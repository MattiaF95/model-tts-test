# LLM-TTS Test

Script Python semplici per testare e confrontare modelli LLM-TTS con reference audio diversi.

L'idea del repo è questa:
- provare lo stesso testo su provider/modelli diversi;
- cambiare reference audio per vedere quanto incide su timbro, enfasi, lingua e naturalezza;
- tenere uno storico pulito dei risultati per confronto rapido.

> Nota: non tutti i test eseguiti sono caricati nel repository. Alcuni sono stati lasciati fuori, ma restano comunque replicabili tramite le demo online linkate sotto.

## Modelli testati

### <img src="./assets/icons/Mistral_AI_logo_(2025–).svg" height="20" alt="Mistral" /> Voxtral TTS
- Testato in locale via API Mistral.
- È quello che, nei test fatti, ha dato il risultato migliore quando il reference audio era buono.
- Supporta voice cloning zero-shot e usa molto il reference come guida per lingua ed enfasi.

Link utili:
- Demo / Studio: [https://console.mistral.ai/build/audio/text-to-speech](https://console.mistral.ai/build/audio/text-to-speech)
- Doc API: [https://docs.mistral.ai/](https://docs.mistral.ai/)
- News / overview: [https://mistral.ai/news/voxtral-tts/](https://mistral.ai/news/voxtral-tts/)
- Model card: [https://huggingface.co/mistralai/Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)

### <img src="./assets/icons/qwen3-logo.webp" height="20" alt="Qwen3" /> Qwen3-TTS
- Testato via DeepInfra e demo web.
- Supporta italiano nativo, preset voices e voice cloning.
- Nel mio test la qualità è risultata meno solida di Voxtral, soprattutto su enfasi e punteggiatura.

Link utili:
- Demo HF: [https://huggingface.co/spaces/Qwen/Qwen3-TTS](https://huggingface.co/spaces/Qwen/Qwen3-TTS)
- Demo / API DeepInfra: [https://deepinfra.com/Qwen/Qwen3-TTS](https://deepinfra.com/Qwen/Qwen3-TTS)
- Playground alternativo: [https://deapi.ai/playground/text-to-speech?model=Qwen3_TTS_12Hz_1_7B_CustomVoice](https://deapi.ai/playground/text-to-speech?model=Qwen3_TTS_12Hz_1_7B_CustomVoice)
- Technical report: [https://arxiv.org/abs/2601.15621](https://arxiv.org/abs/2601.15621)
- Repo ufficiale: [https://github.com/QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS)

### <img src="./assets/icons/NVIDIA_logo.svg" height="20" alt="NVIDIA" /> Magpie TTS
- Lo provo tramite link pubblico, quindi si testa gratis nei limiti concessi dalla demo.
- Il risultato, per ora, è decente.

Link utili:
- Demo HF: [https://huggingface.co/spaces/nvidia/magpie_tts_multilingual_demo](https://huggingface.co/spaces/nvidia/magpie_tts_multilingual_demo)
- Model card: [https://huggingface.co/nvidia/magpie_tts_multilingual_357m](https://huggingface.co/nvidia/magpie_tts_multilingual_357m)

## Script

- `magpie-test.py`: prova Magpie via `gradio_client`.
- `test-llm-tts.py`: genera audio con Voxtral tramite API Mistral.
- `test-tts-qwen3.py`: usa DeepInfra per creare una voce custom e sintetizzare il testo con Qwen3-TTS.

## Struttura

- `Testo.txt`: testo di input da sintetizzare.
- `audio_mp3_riferimento/`: reference audio usati per i confronti.
- `output_audio_mp3/`: output generati dai test.
- `assets/icons/`: icone usate nel README.

## Setup minimo

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` contiene solo le dipendenze dirette che servono per replicare il progetto, quindi se vuoi rifare l'ambiente ti basta quello.

## Variabili ambiente

Per l'ambiente uso `.env.example`: lo copi in `.env` e ci inserisci le tue chiavi API.

- `MISTRAL_API_KEY`: per Voxtral.
- `DEEPINFRA_TOKEN`: per Qwen3-TTS via DeepInfra.

## Esecuzione

```bash
python3 magpie-test.py
python3 test-llm-tts.py
python3 test-tts-qwen3.py
```

## Note pratiche

- Gli script lavorano meglio se il reference audio è pulito, breve e coerente con la voce attesa.
- Molta differenza la fa il testo in ingresso: i modelli LLM-TTS riescono a modulare e dare enfasi migliore seguendo la punteggiatura; meglio è gestita, compresa quella dei dialoghi, migliore sarà il risultato.
- Per Qwen3 il risultato cambia molto tra preset voice e voice clonata. Test effettuati anche con le demo online linkate sopra.
- Per Voxtral il reference audio pesa tantissimo su lingua, ritmo ed enfasi; tra i modelli testati è quello che mi ha dato l'output migliore.
- Per divertirmi ho usato la voce del mitico Luca Ward ed il risultato è impressionante!

## Cosa aspettarsi

- **Magpie**: testabile gratis tramite link pubblico, nei limiti concessi dalla demo; il risultato è decente.
- **Qwen3-TTS**: testabile facilmente con i tool online; il risultato è nella media.
- **Voxtral**: è il migliore tra quelli provati.

## Come testarlo

1. Scegli un testo breve ma abbastanza espressivo e salvalo in `Testo.txt`.
2. Metti 2 o 3 reference audio in `audio_mp3_riferimento/`.
3. Crea il virtual environment e installa le dipendenze con `requirements.txt`.
4. Copia `.env.example` in `.env` e inserisci le chiavi necessarie.
5. Lancia gli script usando lo stesso testo per ogni modello.
6. Confronta gli output in `output_audio_mp3/` su pronuncia, pause, enfasi, accento e naturalezza.
7. Se un test non è presente nel repo o da errori, rifallo usando i link delle demo online riportati sopra.

## Crediti

- Test, note e raccolta risultati: [@MattiaF95](https://github.com/MattiaF95)
