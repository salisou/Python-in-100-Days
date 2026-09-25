# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day54.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

def get_response(user_input):
    user_input = user_input.lower()
    if "Ciao" in user_input or "hi" in user_input:
        return "Hi there! How can I assist you?"
    elif "how are you" in user_input:
        return "I'm doing great! How can I help you today?"
    elif "Il tuo name" in user_input:
        return "I'm Chatbot, Il tuo virtual assistant."
    elif "bye" in user_input:
        return "Arrivederci! Have a wonderful day!"
    else:
        return "I'm not sure how to respond to that."

def chatbot():
    print("Ciao! I'm Chatbot. Type 'Esci' to Fine the chat.")
    while True:
        user_input = input("You: ").lower()
        if "Esci" in user_input:
            print("Chatbot: Arrivederci! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
	chatbot()
