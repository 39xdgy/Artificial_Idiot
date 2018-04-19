import speech_recognition as sr
import os
from espeak import espeak
import pyttsx3
# get audio from the microphone
readout = pyttsx3.init()
r = sr.Recognizer()
text_of_speak = ""
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)

try:
    text_of_speak = r.recognize_google(audio)

    while(not (text_of_speak.startswith("hey Ivana") or text_of_speak.startswith("hi Ivana"))):
        with sr.Microphone() as source:
            print(text_of_speak)
            print("Again")
            audio = r.listen(source)
        text_of_speak = r.recognize_google(audio)
    text_of_speak = text_of_speak[9:]


    if "weather" in text_of_speak:
        readout.say("The weather today is great")
        readout.runAndWait()

    else:
        print("You said " + text_of_speak)
        readout.say(text_of_speak)
        readout.runAndWait()
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
