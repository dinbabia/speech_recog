
import speech_recognition as sr
import webbrowser
from datetime import datetime
import time
import playsound
import os
import random
from gtts import gTTS

class Alexa:
    
    def __init__(self):
        self.users = ["din", "theo"]
        self.user = ""
    
    def alexa_speak(self,audio_string):
        tts = gTTS(text=audio_string, lang='en')  
        r = random.randint(1,10000)  
        audio_file = 'audio-' + str(r) + '.mp3'
        tts.save(f"src/{audio_file}")
        playsound.playsound(f"src/{audio_file}")
        os.remove(f"src/{audio_file}")
        
    def respond(self,voice_data):
        if 'your name' in voice_data:
            self.alexa_speak('My name is, Alexa.')  
            
        elif 'love you' in voice_data:
            self.alexa_speak('I love you too')
            
        elif 'what time' in voice_data:
            time = datetime.now()
            self.alexa_speak("Time is: " + time.strftime("%I:%M%p"))
            
        elif 'how' in voice_data and 'you' in voice_data:
            self.alexa_speak("I'm fine sir! Thank you!")
            
        elif 'search' in voice_data:
            search =self.record_audio('What do you want me to search?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            self.alexa_speak("Here is my result")
            
        elif 'find location' in voice_data:
            location =self.record_audio('What location do you want me to search?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            self.alexa_speak("Here is my result")
        
        elif 'switch' and 'user' in voice_data:
            
            self.alexa_speak("Which user do you want to switch?")
            
            while True:
                user =self.record_audio('Just say one for din, and two for theo.')
                if user == "one":
                    user_number = 1
                    break
                elif user =="two":
                    user_number = 2
                    break
                elif user == "exit":
                    return "exit"
                
            
            self.alexa_speak(f"Switching user to {self.users[user_number -1]}")
            self.user = self.users[user_number -1]
            return self.users[user_number -1]
            
        elif 'exit' in voice_data:
            self.alexa_speak('Goodbye!')
            exit()
            
    def record_audio(self, ask = False):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            
            if ask:
                
                self.alexa_speak(ask)
                
            audio = r.listen(source, phrase_time_limit=3)
            voice_data = ''
            try:
                text = r.recognize_google(audio)
                voice_data =text
            except:
                self.alexa_speak("I can't understand you...")
                
            return voice_data
