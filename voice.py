from gtts import gTTS

def GenerateVoice(text:str, output:str):
    voice = gTTS(text, lang='en', tld='co.in', slow=False)
    voice.save(f"raw/audios/{output}.mp3")

#generateVoice("test", "The one who ignorantly takes the entire armrest.")