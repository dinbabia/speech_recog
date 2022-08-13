from alexa import Alexa
import playsound
import speech_recognition as sr


class UserVoice(Alexa):
    
    
    def __init__(self):
        super().__init__()
        self.user_directory = "src/mp3"
        
    def user_welcome(self, user):
        playsound.playsound(f"{self.user_directory}/{user}/welcome.wav")
        
    def record_audio(self, user, ask=False):
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            audio = r.listen(source, phrase_time_limit=3)
            voice_data = ''
            try:
                text = r.recognize_google(audio)
                voice_data =text
            except:
                playsound.playsound(f"{self.user_directory}/{user}/not_clear.wav")          
            return voice_data
        
    def respond(self, user , voice_data):
        if "your name" in voice_data:
            playsound.playsound(f"{self.user_directory}/{user}/my_name.wav")
        elif 'love you' in voice_data:
            playsound.playsound(f"{self.user_directory}/{user}/i_love_you_too.wav")
        elif 'how' in voice_data and 'you' in voice_data:
            playsound.playsound(f"{self.user_directory}/{user}/how_are_you.wav")
        elif 'exit' in voice_data:
            playsound.playsound(f"{self.user_directory}/{user}/exit.wav")
            exit()