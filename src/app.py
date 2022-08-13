import alexa
import time
import user_voice


alexa = alexa.Alexa()
app_start = True
user_action = user_voice.UserVoice()


while app_start:
    alexa.alexa_speak("Welcome sir! How can I help you?")
    
    while True:
        time.sleep(1)
        voice_data = alexa.record_audio()
        if alexa.respond(voice_data) in alexa.users:
            break
    
    while True:   

        user_action.user_welcome(alexa.user)
        
        while True:
            voice_data = user_action.record_audio(alexa.user)
            user_action.respond(alexa.user, voice_data)


          