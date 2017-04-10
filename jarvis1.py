#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        os.system('afplay /System/Library/Sounds/Purr.aiff')
        audio = r.listen(source)

 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        #print("You said: " + data)
    except sr.UnknownValueError:
#        speak ("Google Speech Recognition could not understand audio")
        speak ("I din't understand you. Could you repeat?")

        data = "ouch"

    except sr.RequestError as e:
        temp = "Could not request results from Google Speech Recognition service; {0}".format(e)
        speak (temp)
        data = "ouch"
 
    os.system('afplay /System/Library/Sounds/Sosumi.aiff')
    
    return data
 
def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    if "goodbye" in data:
        speak("I don't belive you wanna leave me!")
        quit()
 
    if "what time is it" in data:
        speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Andrey, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
 
# initialization
time.sleep(2)
speak("Hello. Please start speaking and I will record everything you say.")
note = ""

while 1:
    # старт таймера
    begin_time = time.time()
    
    data = recordAudio()
    note = note + data + "\n"
    speak(data)
    jarvis(data)

    end_time = time.time()
    print(end_time - begin_time)
    print (note)