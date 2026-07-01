# TTS Test

Script Python semplici per testare e confrontare modelli LLM-TTS con reference audio diversi.

L'idea del repo e' questa:
- provare lo stesso testo su provider/modelli diversi;
- cambiare reference audio per vedere quanto incide su timbro, enfasi, lingua e naturalezza;
- tenere uno storico pulito dei risultati per confronto rapido.

## Modelli testati

### Voxtral TTS
- Testato in locale via API Mistral.
- E' quello che, nei test fatti, ha dato il risultato migliore quando il reference audio era buono.
- Supporta voice cloning zero-shot e usa molto il reference come guida per lingua ed enfasi.

Link utili:
- Demo / Studio: https://console.mistral.ai/build/audio/text-to-speech
- Doc API: https://docs.mistral.ai/
- News / overview: https://mistral.ai/news/voxtral-tts/
- Model card: https://huggingface.co/mistralai/Voxtral-4B-TTS-2603

### Qwen3-TTS
- Testato via DeepInfra e demo web.
- Supporta italiano nativo, preset voices e voice cloning.
- Nel mio test la qualita' e' risultata meno solida di Voxtral, soprattutto su enfasi e punteggiatura.

Link utili:
- Demo HF: https://huggingface.co/spaces/Qwen/Qwen3-TTS
- Demo / API DeepInfra: https://deepinfra.com/Qwen/Qwen3-TTS
- Playground alternativo: https://deapi.ai/playground/text-to-speech?model=Qwen3_TTS_12Hz_1_7B_CustomVoice
- Technical report: https://arxiv.org/abs/2601.15621
- Repo ufficiale: https://github.com/QwenLM/Qwen3-TTS

### Magpie TTS
- Presente per storico e confronto.
- La demo/modello non e' stato comodo da usare gratis al momento del test, quindi non lo considero il punto di riferimento del repo.

Link utili:
- Demo HF: https://huggingface.co/spaces/nvidia/magpie_tts_multilingual_demo
- Model card: https://huggingface.co/nvidia/magpie_tts_multilingual_357m

## Script

- `magpie-test.py`: prova Magpie via `gradio_client`.
- `test-llm-tts.py`: genera audio con Voxtral tramite API Mistral.
- `test-tts-qwen3.py`: usa DeepInfra per creare una voce custom e sintetizzare il testo con Qwen3-TTS.

## Struttura

- `Testo.txt`: testo di input da sintetizzare.
- `audio_test/riferimento/`: reference audio usati per i confronti.
- `audio_test/output/`: output generati dai test.
- `test-tts/`: ambiente Python locale.

Nota sui path:
- gli script sono nati con path hardcoded tipo `audio_mp3_riferimento/` e `output_audio_mp3/`;
- nel repo gli esempi disponibili ora stanno in `audio_test/`, quindi se vuoi rifare i test senza toccare il codice, allinea i nomi delle cartelle.

## Setup minimo

```bash
python -m venv .venv
source .venv/bin/activate
pip install requests python-dotenv gradio_client mistralai
```

## Variabili ambiente

Non mettere mai chiavi nel repo. Usa un file `.env` locale.

- `MISTRAL_API_KEY`: per Voxtral.
- `DEEPINFRA_TOKEN`: per Qwen3-TTS via DeepInfra.

## Esecuzione

```bash
python magpie-test.py
python test-llm-tts.py
python test-tts-qwen3.py
```

Nota pratica:
- gli script lavorano meglio se il reference audio e' pulito, breve e coerente con la voce attesa;
- per Qwen3 il risultato cambia molto tra preset voice e voice clonata;
- per Voxtral il reference audio pesa tantissimo su lingua, ritmo ed enfasi.

## Cosa aspettarsi

- Magpie: utile per storico, ma non sempre testabile gratis.
- Qwen3-TTS: funziona, ma l'output puo' risultare meno naturale.
- Voxtral: nei test fatti e' stato il migliore, soprattutto con reference audio buono.

## Replica del progetto

Se vuoi rifarlo da zero:
1. scegli un testo breve ma abbastanza espressivo;
2. prepara 2 o 3 reference audio diversi;
3. lancia gli script sullo stesso prompt;
4. confronta gli output su pronuncia, pause, enfasi, accento e naturalezza;
5. salva sempre input e output con nomi chiari.

## Crediti

- Analisi, test e raccolta note: Mattia Fazi.
- Se vuoi attribuire il lavoro in modo pubblico, una riga di credito al creatore ci sta ed e' normale per un repo di confronto.

## Nota

Questo repo e' pubblico: niente segreti, niente token nel codice, niente file sensibili committati.
