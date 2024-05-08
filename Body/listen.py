import speech_recognition as sr 
from deep_translator import GoogleTranslator

def Listen():
    
    r = sr.Recognizer()
      
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)
      
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")
    except:
          return ""

    query = str(query).lower()
    return query


def TranslationHinToEng(Text):
    line = str(Text)
    translator = GoogleTranslator(source='auto', target='en')
    result = translator.translate(line)
    data = result
    print(f"You: {data}.")
    return data



def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data
