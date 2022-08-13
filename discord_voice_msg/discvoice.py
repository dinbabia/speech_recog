import requests
import speech_recognition as sr
import time
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        
        if ask:
            alexis_speak(ask)
        audio = r.listen(source, timeout = 1,phrase_time_limit=3)
        voice_data = ''
        try:
            text = r.recognize_google(audio)
            voice_data =text
        except:
            alexis_speak("I can't understand you...")
            
        return voice_data

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')  
    r = random.randint(1,10000)  
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def message_data(msg):
    payload = {
        "content" : f'{msg}'
        
    }

    headers = {
        "authorization" : "ODc3NzI4ODIyOTExNDQyOTg0.Yepn7w.aBYm3-KFuyd_00_kggjwDFZX-T8"
    }
    
    # Insert Discord API Here
    api_my_server = ""
    api_qa_gc = ""

    r = requests.post(f"{api_my_server}", data=payload, headers=headers)

alexis_speak("How can I help you?")
while True:
    time.sleep(1)
    voice_data = record_audio()
    message_data(voice_data)
    exit()

