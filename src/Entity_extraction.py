import spacy
import re

# Load spaCy's English language model
nlp = spacy.load("models/fine_tuned_ner_model")

def entity_extraction(query):
    # Process the text
    doc = nlp(query)

    # Extract entities
    entities = [re.sub(r"[^\w\s]", "", ent.text).lower() for ent in doc.ents]
    return entities



if __name__ == "__main__": 
    while (user_query := input("You: ").lower()) not in ["quit", "back", "thats it", "bye"]:
        entity_extraction(user_query)
