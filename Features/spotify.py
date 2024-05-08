import spotipy
import spotipy.util as util
import speech_recognition as sr
import os

from dotenv import load_dotenv
load_dotenv()

# Define your Spotify username
username = os.getenv("SPOTIFY_USERNAME")

# Define the scope of the authorization for the user
scope = 'user-modify-playback-state user-read-playback-state user-library-read user-top-read playlist-modify-public'

# Load Spotify API credentials from environment variables
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_url = os.getenv("SPOTIFY_REDIRECT_URI")

# Get an access token for the user using the Spotify API
token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id, 
                                   client_secret=client_secret, 
                                   redirect_uri=redirect_url)

# Create a Spotipy instance with the access token
sp = spotipy.Spotify(auth=token)

# Define a function to recognize speech input

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak now...')
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio)
        print(f'You said: {speech}')
        return speech
    except Exception as e:
        print(f'Error: {str(e)}')
        return None

# Define a function to search for a song on Spotify
def search_song(song_name):
    results = sp.search(q=song_name, type='track')
    items = results['tracks']['items']
    if len(items) > 0:
        song_uri = items[0]['uri']
        return song_uri
    else:
        return None

# Define the main function
def spotify_main():
    while True:
        speech = recognize_speech()
        if speech:
            if 'play' in speech:
                song_name = speech.replace('play', '').strip()
                song_uri = search_song(song_name)
                if song_uri:
                    sp.start_playback(uris=[song_uri])
                    print(f'Now playing: {song_name}')
                else:
                    print(f"Sorry, I couldn't find a song with that name.")
            elif 'stop' in speech:
                sp.pause_playback()
                print('Music stopped.')
            elif 'next' in speech:
                sp.next_track()
                print('Next track.')
            elif 'previous' in speech:
                sp.previous_track()
                print('Previous track.')
            elif 'resume' in speech:
                sp.start_playback()
                print('Music resumed.')
            elif 'shuffle' in speech:
                sp.shuffle(True)
                print('Shuffle mode turned on.')
            elif 'unshuffle' in speech:
                sp.shuffle(False)
                print('Shuffle mode turned off.')
            elif 'repeat' in speech:
                sp.repeat('context')
                print('Repeat mode turned on.')
            elif 'unrepeat' in speech:
                sp.repeat('off')
                print('Repeat mode turned off.')
            elif 'volume up' in speech:
                volume = sp.current_playback()['device']['volume_percent']
                if volume < 100:
                    volume += 10
                    sp.volume(volume)
                    print(f'Volume increased to {volume}%.')
                else:
                    print('Maximum volume reached.')
            elif 'volume down' in speech:
                volume = sp.current_playback()['device']['volume_percent']
                if volume > 0:
                    volume -= 10
                    sp.volume(volume)
                    print(f'Volume decreased to {volume}%.')
                else:
                    print('Minimum volume reached.')
            else:
                None

