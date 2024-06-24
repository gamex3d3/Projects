from gtts import gTTS

language = "fr"
text = "bonjour! je m'appelle guy"

speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
speech.save("txts.mp3")