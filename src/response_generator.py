import sys
import os
import random
import json
import speech_recognition as sr
from gtts import gTTS
import io
from pydub import AudioSegment
from pydub.playback import play

# Setting up the directory to the main folder "College_AI"
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_path)

from DataBase.context_manager import store_context_db, get_context_db  # Import SQLite context functions
from src.Intent_classification import intent_prediction  # Import intent prediction function
from src.Entity_extraction import entity_extraction  # Import entity extraction function

# Load responses from JSON file
def load_responses(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

file_path = os.path.join(os.path.dirname(__file__), "../response_data/responses.json")
response_data = load_responses(file_path)

# ✅ Generate response based on query or follow-up (No follow-up storage here)
def generate_response(user_id, user_query):
    """
    Generates a response based on user query.
    Does not store follow-up questions, only intent & entities.
    """
    try:
        intent = intent_prediction(user_query)  # Predict intent
        print("Intent:", intent)  # debugging
    except Exception as e:
        print(f"Error in intent prediction: {e}")
        intent = "DEFAULT"  # Default to a generic response

    try:
        entities = entity_extraction(user_query)  # Extract entities
    except Exception as e:
        print(f"Error in entity extraction: {e}")
        entities = []  # Default to empty entity list

    responses = []

    if intent in response_data:
        intent_responses = response_data[intent]

        if not entities:
            response = random.choice(intent_responses.get("default", ["I'm not sure."]))
        else:
            response = []
            for entity in entities:
                if entity in intent_responses:
                    response.append(random.choice(intent_responses[entity]))
                else:
                    response.append(random.choice(intent_responses.get("default", ["I'm not sure."])))
            response = " ".join(response)

        responses.append(response)

        # ✅ Store intent & entities ONLY (No follow-up question storage)
        if "followup" in intent_responses:
            handle_context(user_id, "store", intent, entities)  # Store intent & entities only

    else:
        responses.append(random.choice(response_data["DEFAULT"]["default"]))

    return "\n".join(responses)

# ✅ Find follow-up question in JSON (Does NOT store anything)
def followUp_question(intent):
    """
    Retrieves follow-up question from JSON if available.
    """
    intent_responses = response_data.get(intent, {})
    followup_question = intent_responses.get("followup")
    return random.choice(followup_question) if followup_question else None

# ✅ Store & retrieve only intent & entities (No follow-up question storage)
def handle_context(user_id, action, intent=None, entities=None):
    """
    Manages user-specific context for conversation continuity.
    Stores only user_id, intent, and entities.
    """
    try:
        if action == "store":
            store_context_db(user_id, intent, entities)  # Store intent & entities only
        elif action == "retrieve":
            return get_context_db(user_id)  # Retrieve intent & entities only
        elif action == "clear":
            store_context_db(user_id, "", {})  # Clear intent & entities
    except Exception as e:
        print(f"Error in context handling: {e}")

# Function to convert text to speech and play it from memory without saving a file
def text_to_speech(response_text):
    """Convert text to speech and play it from memory without saving a file."""
    if not response_text:
        response_text = "I'm sorry, I could not understand the question."
    tts = gTTS(text=response_text, lang='en', slow=False)
    
    # Store the speech output in memory instead of a file
    audio_stream = io.BytesIO()
    tts.write_to_fp(audio_stream)
    
    # Load audio from memory
    audio_stream.seek(0)
    audio = AudioSegment.from_file(audio_stream, format="mp3")
    
    # Adjust the pitch
    octaves = 0.5  # Increase pitch by half an octave
    new_sample_rate = int(audio.frame_rate * (2.0 ** octaves))
    high_pitch_audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})
    high_pitch_audio = high_pitch_audio.set_frame_rate(44100)
    
    # Play the modified audio directly from memory
    play(high_pitch_audio)

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

# ✅ Main chatbot function with improved conversation flow
def chatbot_flow():
    """
    Manages the conversation flow properly.
    Uses follow-up questions as the next input when user says "yes".
    """
    while True:
        user_id = input("Enter your user ID (or type 'exit' to quit): ")

        if user_id.lower() == "exit":
            print("Exiting chatbot.")
            break

        while True:
            print(f"You ({user_id}): Say something... (Say 'quit', 'bye', or 'exit' to quit)")
            user_query = speech_to_text()

            if user_query.lower() in ["quit", "bye", "exit"]:
                print(f"Assistant ({user_id}): Goodbye!")
                text_to_speech("Goodbye!")
                handle_context(user_id, "clear")
                break  
            
            # ✅ Step 2: Process the user query normally
            response = generate_response(user_id, user_query)
            print(f"Assistant ({user_id}): {response}")
            text_to_speech(response)
            
            # ✅ Step 1: Check if a follow-up exists
            context = handle_context(user_id, "retrieve")
            if context:
                stored_intent = context.get("intent")
                print("Context:", context) # debugging
                if stored_intent:
                    followup_question = followUp_question(stored_intent)
                    if followup_question:
                        print(f"Assistant ({user_id}): {followup_question}")
                        text_to_speech(followup_question)
                        user_query = speech_to_text()  # Take user's input for the follow-up

                        # ✅ If user says "yes", use the follow-up question as the input
                        if user_query.lower() in ["yes", "yeah", "yep", "sure", "okay"]:
                            user_query = followup_question  # Treat follow-up as input
                            response = generate_response(user_id, user_query)
                            handle_context(user_id, "clear")  # Clear intent & entities
                            print(f"Assistant ({user_id}): {response}")
                            text_to_speech(response)
                            continue

                        # ✅ If user says "no", clear context & move on
                        elif user_query.lower() in ["no", "nope", "nah", "not really"]:
                            handle_context(user_id, "clear")
                            print(f"Assistant ({user_id}): Alright, let me know if you have any other questions.")
                            text_to_speech("Alright, let me know if you have any other questions.")
                            continue
                        else:
                            response = generate_response(user_id, user_query)
                            print(f"Assistant ({user_id}): {response}")
                            text_to_speech(response)

# ✅ Run the chatbot
if __name__ == "__main__":
    chatbot_flow()