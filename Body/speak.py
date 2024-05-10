import pyttsx3
import platform
import os

system_platform = platform.system()

def Speak(Text, lang='en'):
    
    if system_platform == 'Windows':
        engine = pyttsx3.init ("sapi5")
        voices = engine.getProperty('voices')
        engine.setProperty ('voices' ,voices[1].id)
        engine.setProperty('rate' ,170)
        print()
        print(f"NOVA : {Text}.")
        print()
        engine.say(Text)
        #engine.save_to_file("")
        engine.runAndWait()
    elif system_platform == 'Darwin':  # macOS
        print()
        print(f"NOVA : {Text}.")
        print()
        cmd = f'say "{Text}"'
        os.system(cmd)
    else:
        print("Text-to-speech is not supported on this platform.")


#Speak("Hello, I am Nova. How can I help you?")
