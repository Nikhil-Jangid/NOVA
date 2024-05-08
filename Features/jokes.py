import requests

def get_jokes():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        joke_data = response.json()
        joke_setup = joke_data["setup"]
        joke_punchline = joke_data["punchline"]
        return f"{joke_setup} {joke_punchline}"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")
        return "Failed to fetch joke"
