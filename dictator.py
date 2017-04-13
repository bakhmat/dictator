#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from time import ctime
import time
from time import gmtime, strftime
import os
from gtts import gTTS


def boldprint(text):
    # Just print in bold to avoide distractions from warning messages and other non-relevant stuff.
    print ('\033[1m' + str(text) + '\033[0m')


def speak(text2pronounce):
    # Pronounce the text using gTTS library which is based on Google synthesiser.
    # It saves the file on the disk and playback it as a next step.
    if text2pronounce != "":
        boldprint(text2pronounce)
        tts = gTTS(text=text2pronounce, lang='en')
        tts.save("audio.mp3")
        os.system("mpg321 audio.mp3")

 
def recordAudio(timestamp):
    # Record Audio

    r = sr.Recognizer()

    with sr.Microphone() as source:
        boldprint("Say something!")
        os.system('afplay /System/Library/Sounds/Purr.aiff')
        audio = r.listen(source)

    with open("microphone-input "+timestamp+".wav", "wb") as f:
        f.write(audio.get_wav_data())

    return audio

def recognizeAudio(audioWave,timestamp):
    # Speech recognition using Google Speech Recognition

    r = sr.Recognizer()

    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audioWave)

    except sr.UnknownValueError:
        os.system('afplay /System/Library/Sounds/Sosumi.aiff')
        speak ("I din't understand you. Could you repeat?")
        boldprint("I din't understand you. Could you repeat?")

    except sr.RequestError as e:
        os.system('afplay /System/Library/Sounds/Sosumi.aiff')
        temp = "Could not request results from Google Speech Recognition service; {0}".format(e)
        speak (temp)
        boldprint(temp)
    
    return data
 
def command_processing(data):
    if "how are you" in data:
        speak("I am fine")

    if "goodbye" in data:
        speak("Have a nice day!")
        quit()
 
    if "what time is it" in data:
        speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on pal, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

    if "repeat" and "slave" in data:
        playback_mode(note)
    


def record_mode():

    time.sleep(2)
    #speak("Hello. Please start speaking and I will record everything you say.")
    speak("You are in Record mode now. Please start dɪkˈteɪ ʃən.")
    global note
    note = ""

    while True:
        # timer start 
        # begin_time = time.time()
        # This timer might be needed for debugging and analyzing recognize_google function behaviour.

        # strftime gives us timestamp (currenttime) for our records - both original audio and recognized text.
        currenttime = strftime("%d %b %Y %H-%M-%S GMT", gmtime())

        audio = recordAudio(currenttime)
        data = recognizeAudio(audio,currenttime)

        note = note + data + " (" + currenttime + ")\n"
        

        speak(data)
        command_processing(data)

        # end_time = time.time()
        # boldprint(end_time - begin_time)
        boldprint (note)


        # Record all recognised text in note.txt file
        # Will be replaced by storage in a MySQL database in next versions.
        text_file = open('note.txt', 'w')
        text_file.write(note)
        text_file.close()


def playback_mode(text2pronounce):

    speak("You are in Playback mode now. ")
    # while True:
    
    speak(text2pronounce)

record_mode()













