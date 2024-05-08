import os
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
import pyowm

# Load environment variables
load_dotenv()

def get_weather_details(location):
    try:
        # Get geolocation
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(location)

        # Check if location is found
        if not location:
            raise ValueError("Location not found")

        # Get API key from environment variables
        api_key = os.getenv("OWM_API_KEY")
        if not api_key:
            raise ValueError("OWM_API_KEY environment variable is not set")

        # Get weather details
        owm = pyowm.OWM(api_key)
        observation = owm.weather_at_coords(location.latitude, location.longitude)
        weather = observation.get_weather()

        # Return weather data
        return {
            'location': location.address,
            'temperature': weather.get_temperature('celsius')['temp'],
            'humidity': weather.get_humidity(),
            'status': weather.get_status()
        }
    except Exception as e:
        return {'error': str(e)}
