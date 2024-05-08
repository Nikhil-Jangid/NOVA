import requests

def translate(phrase, target_language):
    # Make a GET request to the Google Translate API
    response = requests.get("https://translation.googleapis.com/language/translate/v2", 
                            params={"q": phrase, 
                                    "target": target_language, 
                                    "format": "text", 
                                    "source": "en",
                                    "key": "<your_google_translate_api_key>"})
    # Extract the translation from the response JSON
    translation = response.json()["data"]["translations"][0]["translatedText"]
    return translation