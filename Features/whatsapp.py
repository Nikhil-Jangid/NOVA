from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import speech_recognition as sr

def convert_voice_to_text(prompt):
    # Record voice input
    os.system(f'say "{prompt}"')  # Voice prompt to start speaking
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    # Convert voice to text
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error: {str(e)}")
    return None

def send_whatsapp_message():
    # Initialize WebDriver
    driver = webdriver.Safari()
    driver.get('https://web.whatsapp.com')

    # Load saved cookies
    try:
        cookies = open('cookies.txt', 'r')
        for cookie in cookies:
            driver.add_cookie(eval(cookie))
        cookies.close()
    except FileNotFoundError:
        pass

    # Refresh the page after loading cookies
    driver.refresh()
    time.sleep(5)

    # Ask for recipient's name and message through voice input
    recipient_name = convert_voice_to_text("Please dictate the recipient's name:")
    message_text = convert_voice_to_text("Please dictate the message you want to send:")

    # Identify and Select Chat
    time.sleep(10)
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(recipient_name)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)

    # Send Message
    message_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
    message_input.send_keys(message_text)
    message_input.send_keys(Keys.ENTER)

    # Save cookies for future use
    cookies_file = open('cookies.txt', 'w')
    cookies_file.write(str(driver.get_cookies()))
    cookies_file.close()

    # Quit WebDriver
    time.sleep(2)
    driver.quit()

# Main program execution
send_whatsapp_message()
