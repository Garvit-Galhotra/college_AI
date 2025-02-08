from gtts import gTTS
import io
import pygame
from response_generator import generate_response

def text_to_speech(response_text):
    """Convert text to speech and play it from memory without saving a file."""
    if not response_text:
        response_text = "I'm sorry, I could not understand the question."
    tts = gTTS(text=response_text, lang='en')
    
    # Store the speech output in memory instead of a file
    audio_stream = io.BytesIO()
    tts.write_to_fp(audio_stream)
    
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load audio from memory
    audio_stream.seek(0)
    pygame.mixer.music.load(audio_stream, "mp3")
    pygame.mixer.music.play()
    
    # Wait until playback is done
    while pygame.mixer.music.get_busy():
        continue

import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening...")
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        print("Could not understand the audio, please try again.")
        return None
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        return None
    
if __name__ == "__main__":
    last_response = None
    repeat_keywords = ["repeat", "say that again", "i didn't understand", "can you repeat", "what did you say", "come again"]
    exit_keywords = ["quit", "back", "that's it", "bye", "exit", "stop"]

    while True:
        print("Say something... (Say 'quit', 'back', 'that's it', or 'bye' to exit)")
        user_query = speech_to_text()
        print(user_query)
        if user_query and any(keyword in user_query for keyword in exit_keywords):
            print("Goodbye!")
            text_to_speech("Goodbye! I will be here If you need help with anything")
            break
        if user_query and any(keyword in user_query for keyword in repeat_keywords):
            if last_response:
                text_to_speech(last_response)
            else:
                pass
        elif user_query:  # Proceed only if speech was successfully converted to text
            response = generate_response(user_query)
            last_response=response
            text_to_speech(response)
