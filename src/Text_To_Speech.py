from gtts import gTTS
import io
import pygame
from response_generator import generate_response

def text_to_speech(response_text):
    """Convert text to speech and play it from memory without saving a file."""
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
        print("Listening...")
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
    while True:
        print("Say something... (Say 'quit', 'back', 'that's it', or 'bye' to exit)")
        user_query = speech_to_text()
        
        if user_query in ["quit", "back", "thats it", "bye"]:
            print("Goodbye!")
            break

        if user_query:  # Proceed only if speech was successfully converted to text
            response = generate_response(user_query)
            text_to_speech(response)
