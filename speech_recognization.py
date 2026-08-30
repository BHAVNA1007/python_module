"""import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak...")
    audio = r.listen(source)

with open("voice.wav", "wb") as f:
    f.write(audio.get_wav_data())

print("Audio saved as voice.wav")"""

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak...")
    audio = r.listen(source)

text = r.recognize_google(audio)

print("You said:", text)