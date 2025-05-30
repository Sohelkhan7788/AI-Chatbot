import json
import random
import difflib

# Load intents from JSON file
with open("intents.json", "r") as file:
    intents = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return random.choice(intent["responses"])
    return "I'm not sure I understand. Could you rephrase that?"
