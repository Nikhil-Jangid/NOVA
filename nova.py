from Body.listen import MicExecution
from Body.speak import Speak
from Features.geolocation import city
from Features.weather import get_weather_details
from Features.news import get_news
from Features.jokes import get_jokes
from Features.wikipedia_search import search_wikipedia
from Features.website import open_website
from Brain.ai_brain import generate_response
import datetime

def greet_user():
    Speak("Hello Sir")
    Speak("I'm NOVA, I'm Ready To Assist You Sir.")

def handle_hello():
    Speak("Hello! How can I assist you?")

def handle_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    Speak(f"The time is {now}")

def handle_wikipedia(query):
    Speak("Searching Wikipedia...")
    result = search_wikipedia(query)
    Speak("According to Wikipedia")
    Speak(result)

def handle_weather():
    city_name = city()
    weather_info = get_weather_details(city_name)
    Speak(f"The current temperature in {weather_info['location']} is {weather_info['temperature']} degrees Celsius with {weather_info['status']} and {weather_info['humidity']}% humidity.")

def handle_news():
    news_info = get_news()
    Speak(news_info)

def handle_joke():
    joke = get_jokes()
    Speak(joke)

def main_execution():
    greet_user()

    while True:
        query = MicExecution()
        query = query.replace(".", "")

        if 'hello' in query:
            handle_hello()
        elif 'time' in query:
            handle_time()
        elif 'wikipedia' in query:
            handle_wikipedia(query)
        elif 'weather' in query:
            handle_weather()
        elif 'news' in query:
            handle_news()
        elif 'joke' in query:
            handle_joke()
        elif 'open' in query:
            open_website(query)
        else:
            reply = generate_response(query)
            Speak(reply)

if __name__ == "__main__":
    main_execution()
