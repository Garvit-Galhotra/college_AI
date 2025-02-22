import sys
import os
import random
import json

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_path)

from src.Intent_classification import intent_prediction  # importing intent prediction from intent classification
from src.Entity_extraction import entity_extraction # importing entity extraction function from entityExtraction

# Load responses from JSON file
def load_responses(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
file_path = os.path.join(os.path.dirname(__file__), "../response_data/responses.json")
response_data = load_responses(file_path)

# Function to handle context and follow-up questions
def handle_followup(context, user_response, response_data):
    if context and "followup" in context:
        followup_question = context["followup"]
        if user_response.lower() in ["yes", "yeah", "yep", "sure", "okay"]:
            # Use follow-up question and entities to generate response
            intent_responses = response_data[context["intent"]]
            entities = context["entities"]
            responses = []
            for entity in entities:
                if entity in intent_responses:
                    responses.append(random.choice(intent_responses[entity]))
                else:
                    responses.append(random.choice(intent_responses["default"]))
            if not responses:
                responses.append(random.choice(intent_responses["default"]))
            return "\n".join(responses)
        # if user responds with different question
        elif user_response.lower() in ["no", "nope", "nah", "not really"]:
            return "Alright, let me know if you have any other questions."
        # If user responds with "no", provide a default response
        else:
            return generate_response(user_response)
    return None

# Fetch response based on raw user query
def generate_response(user_query):
    
    responses = []
    global context
    context = None
    # Step 1: Predict Intent
    intent = intent_prediction(user_query)
    
    # Step 2: Extract Entities
    entities = entity_extraction(user_query)

    # Step 3: Retrieve Response
    if intent in response_data:
        intent_responses = response_data[intent]

        if not entities:  # If entities list is empty
            responses.append(random.choice(intent_responses["default"]))
        else:
            for entity in entities:
                if entity in intent_responses:
                    responses.append(random.choice(intent_responses[entity]))
                else:
                    responses.append(random.choice(intent_responses["default"]))
    
        if not responses:
            responses.append(random.choice(intent_responses["default"]))
        
        # Add follow-up question if available
        if "followup" in intent_responses:
            followup_question = random.choice(intent_responses["followup"])
            responses.append(followup_question)
            context = {"intent": intent, "entities": entities, "followup": followup_question}
    else:
        intent = "DEFAULT"
        intent_responses = response_data[intent]
        responses.append(random.choice(intent_responses["default"]))

    response = "\n".join(responses)
    return response

# Example usage
if __name__ == "__main__":
    context = None
    while True:
        user_query = input("You: ")
        if user_query.lower() in ["quit", "exit", "bye"]:
            print("Assistant: Goodbye!")
            break
        if context:
            followup_response = handle_followup(context, user_query, response_data)
            if followup_response:
                print(f"Assistant: {followup_response}")
                context = None
                continue
        response = generate_response(user_query)
        print(f"Assistant: {response}")