from gradio_client import Client

client = Client("nvidia/magpie_tts_multilingual_demo")
result = client.predict(
input_text="""Erano quasi le sette quando Marta sentì quel rumore. Un tonfo sordo, come se qualcosa fosse caduto proprio sopra il soffitto della cucina.
«Hai sentito anche tu?» chiese sottovoce a Luca, che alzò lo sguardo dal libro.
«Sì... ma non c'è nessuno lassù, giusto?»
Si guardarono. La vecchia soffitta non veniva aperta da anni. Marta si alzò lentamente, con il cuore che le batteva più forte a ogni passo. Afferrò la torcia.
«Vieni con me.» La sua voce tremava.
Salii le scale uno dopo l'altro. Il legno scricchiolava. Arrivati davanti alla botola, Marta cercò nel cassetto la chiave arrugginita. Con mani incerte, girò la serratura.
Click.
La botola si aprì lentamente. Un odore di polvere e carta antica invase l'aria.
«Guarda!» esclamò Luca. In un angolo, semi-nascosta da una coperta, c'era una piccola valigia. Marta si chinò, la aprì con cautela.
Dentro c’erano lettere. Decine di lettere.
Lettere di suo nonno alla nonna, mai consegnate.
La voce si spezzò. Marta prese una delle lettere con mano tremante e lesse ad alta voce:
"Mia cara Elena, non so se leggerai mai queste parole, ma ogni giorno lontano da te è una ferita che non smette di bruciare..."
Un silenzio profondo li avvolse.
Poi, quasi d’istinto, Marta sorrise.
«Forse... forse non tutto è andato perso.»""",
	language="it",
	speaker="Jason",
	apply_TN="Do not apply TN",
	api_name="/demo_tts",
)
print(result)