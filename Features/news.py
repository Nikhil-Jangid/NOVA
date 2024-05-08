import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_news():
    # Fetch and return news based on the country code in the environment variable
    country_code = os.getenv('NEWS_COUNTRY_CODE', 'in')  # Default to 'in' (India) if not specified
    news = fetch_news_from_country(country_code)
    return news

def fetch_news_from_country(country_code):
    # Get API key from environment variable
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        print("Error: News API key not found in environment variables.")
        return None
    
    # API endpoint for fetching news headlines
    url = 'https://newsapi.org/v2/top-headlines'
    # Parameters for the API request
    params = {
        'country': country_code,
        'apiKey': api_key
    }
    # Make the API request
    response = requests.get(url, params=params)
    # Check if request was successful
    if response.status_code != 200:
        print(f"Error: Unable to fetch news. Status code: {response.status_code}")
        return None
    # Parse the JSON response
    data = response.json()
    # Extract headlines from the response
    headlines = [article['title'] for article in data['articles']]
    # Join headlines into a single string
    news = '\n'.join(headlines)
    return news
