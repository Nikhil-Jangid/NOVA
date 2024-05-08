import speech_recognition as sr
import pyaudio
import os
from gtts import gTTS
from playsound import playsound

# Define a dictionary of allowed users and their voice sample file paths
allowed_users = {
    "User_1": "path/to/User_1's/voice.wav",
    "User_2": "path/to/User_2's/voice.wav",
    "User_3": "path/to/User_3's/voice.wav"
}

# Define a function to recognize the user's voice
def recognize_user_voice(audio):
    r = sr.Recognizer()
    for user, voice_path in allowed_users.items():
        with sr.AudioFile(voice_path) as source:
            audio_data = r.record(source)
        user_voice = r.recognize_google(audio_data)
        audio_text = r.recognize_google(audio)
        if audio_text == user_voice:
            return user
    return None

# Define a function to respond to the user
def respond(text):
    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang='en')
    tts.save('response.mp3')
    # Play the response using playsound
    playsound('response.mp3')
    os.remove('response.mp3')

# Main function to handle voice recognition and user authentication
def main():
    # Continuously listen for audio input
    while True:
        # Use PyAudio to record audio input from the microphone
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        audio_data = stream.read(2048)
        stream.stop_stream()
        stream.close()
        p.terminate()
        # Use SpeechRecognition to recognize speech from the audio input
        r = sr.Recognizer()
        try:
            audio_text = r.recognize_google(audio_data)
            # Get the allowed user and personalize actions accordingly
            allowed_user = recognize_user_voice(audio_text)
            if allowed_user:
                if allowed_user == "User_1":
                    # Perform actions personalized for User_1
                    respond("Hello User_1, how can I help you?")
                elif allowed_user == "User_2":
                    # Perform actions personalized for User_2
                    respond("Hi User_2, what can I do for you?")
                elif allowed_user == "User_3":
                    # Perform actions personalized for User_3
                    respond("Hey User_3, what do you need?")
            else:
                # If the user's voice is not recognized, respond with an error message
                respond("I'm sorry, I don't recognize your voice.")
        except sr.UnknownValueError:
            # If speech cannot be recognized, respond with an error message
            respond("I'm sorry, I couldn't understand what you said.")
        except sr.RequestError:
            # If there is an issue with the Google Speech Recognition service, respond with an error message
            respond("I'm sorry, there was an issue with the speech recognition service.")
        except Exception as e:
            # Handle other exceptions
            print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
