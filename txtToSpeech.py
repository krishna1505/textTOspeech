
from gtts import gTTS
import os

abc = open("text.txt")
text = abc.read()
language = "en"
obj = gTTS(text = text, lang = language, slow = False)
obj.save("text.mp3")
