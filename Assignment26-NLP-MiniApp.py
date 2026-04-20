import random

print("🤖 Chatbot: Hello! I am your assistant. Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    # Exit condition
    if user == "bye":
        print("🤖 Chatbot: Goodbye! Have a nice day 😊")
        break

    # Greetings
    elif user in ["hi", "hello", "hey"]:
        print("🤖 Chatbot:", random.choice([
            "Hello! 👋",
            "Hi there! 😊",
            "Hey! How can I help you?"
        ]))

    # Asking name
    elif "name" in user:
        print("🤖 Chatbot: I am a simple AI Chatbot created using Python.")

    # Asking about studies
    elif "study" in user or "learn" in user:
        print("🤖 Chatbot: Practice daily, focus on basics, and build projects!")

    # Asking about AI
    elif "ai" in user:
        print("🤖 Chatbot: AI stands for Artificial Intelligence. It helps machines think like humans.")

    # Asking time
    elif "time" in user:
        import datetime
        print("🤖 Chatbot: Current time is", datetime.datetime.now().strftime("%H:%M:%S"))

    # Default response
    else:
        print("🤖 Chatbot:", random.choice([
            "I didn't understand that 🤔",
            "Can you please rephrase?",
            "Interesting... tell me more!"
        ]))