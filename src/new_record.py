import time
import playsound
import os
import pyaudio
import wave

def chooser_user():
    '''Check if the chosen user has its own directory "/src/mp3/{user}"
    @params None
    @return string | user_directory
    '''
    users = ["din", "theo"]

    while True:
        print("Who will be the user to be recorded?")
        print(*users, sep="\n")
        user = input("Your choice: ")

        if not os.path.isdir(f"src/mp3/{user}"):
            os.system('clear')
            print("User not found. Please enter a valid user.")
            continue
        os.system('clear')
        return f"src/mp3/{user}"
        
        

def record_now():
    '''Record an audio and save it to its designated user folder
    '''
    user_dir = chooser_user()
    recording_name = "exit.wav"
    
    audio = pyaudio.PyAudio()
    
    stream = audio.open(format=pyaudio.paInt16, channels =1 , rate=44100, input=True, frames_per_buffer=1024)
    
    frames = []
    
    input("Press Enter to start recording")
    
    for x in range (3,0,-1):
        print(f"Recording starts in {x}")
        time.sleep(1)
    print("Now Recording...Press Ctrl + C to stop recording...")
    time.sleep(1)
    try:
        while True:
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        pass
    
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    sound_file = wave.open(f"{user_dir}/{recording_name}", "wb")
    
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()
    print(f"Currently playing the recording audio with filename: {recording_name}")
    playsound.playsound(f"{user_dir}/{recording_name}")
    
record_now()
    