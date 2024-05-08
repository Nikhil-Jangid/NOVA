import openai
from dotenv import load_dotenv
import os


def load_api_key():
    """Load OpenAI API key from environment variable."""
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")

def initialize_openai():
    """Initialize OpenAI API with loaded API key."""
    openai.api_key = load_api_key()

def load_chat_log():
    """Load chat log from file."""
    with open("DataBase\chat_log.txt", "r") as file:
        return file.read()

def save_chat_log(chat_log):
    """Save chat log to file."""
    with open("DataBase\chat_log.txt", "w") as file:
        file.write(chat_log)

def generate_response(question, chat_log=None):
    """
    Generate response using OpenAI API.

    Args:
    - question (str): User's question.
    - chat_log (str, optional): Chat log. If provided, appends the conversation to the chat log.

    Returns:
    - response (str): Generated response.
    """
    if chat_log is None:
        chat_log = load_chat_log()

    prompt = f"{chat_log}You : {question}\nNOVA : "
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
    )

    answer = response.choices[0].text.strip()
    updated_chat_log = f"{chat_log}\nYou : {question}\nNOVA : {answer}"
    save_chat_log(updated_chat_log)

    return answer
