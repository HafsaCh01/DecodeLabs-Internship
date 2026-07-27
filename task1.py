import random

# Predefined response banks
GREETINGS = ["hello", "hi", "hey", "good morning", "good evening", "salaam", "assalamualaikum"]
FAREWELLS = ["bye", "exit", "quit", "goodbye", "see you", "khuda hafiz"]
THANKS = ["thanks", "thank you", "shukriya"]
HOW_ARE_YOU = ["how are you", "how's it going", "what's up"]

GREETING_RESPONSES = [
    "Hello there! How can I help you today?",
    "Hi! Nice to see you.",
    "Hey! What can I do for you?"
]
FAREWELL_RESPONSES = [
    "Goodbye! Have a great day.",
    "See you later!",
    "Khuda Hafiz! Take care."
]
THANKS_RESPONSES = [
    "You're welcome!",
    "Anytime!",
    "Happy to help."
]
HOW_ARE_YOU_RESPONSES = [
    "I'm just a bunch of if-else statements, but I'm doing great!",
    "Running smoothly, thanks for asking!"
]
DEFAULT_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Sorry, I don't have a rule for that yet.",
    "Hmm, I don't know how to respond to that."
]


def get_response(user_input: str) -> str:
    """Determine chatbot response using if-else / control-flow logic."""
    text = user_input.lower().strip()

    # Rule 1: Greetings
    if any(word in text for word in GREETINGS):
        return random.choice(GREETING_RESPONSES)

    # Rule 2: Exit / farewell commands
    elif any(word in text for word in FAREWELLS):
        return random.choice(FAREWELL_RESPONSES)

    # Rule 3: Thanks
    elif any(word in text for word in THANKS):
        return random.choice(THANKS_RESPONSES)

    # Rule 4: How are you
    elif any(phrase in text for phrase in HOW_ARE_YOU):
        return random.choice(HOW_ARE_YOU_RESPONSES)

    # Rule 5: Name query
    elif "your name" in text:
        return "I'm RuleBot, a simple rule-based chatbot."

    # Default fallback
    else:
        return random.choice(DEFAULT_RESPONSES)


def is_exit_command(user_input: str) -> bool:
    """Check whether the input should terminate the loop."""
    text = user_input.lower().strip()
    return any(word in text for word in FAREWELLS)


def main():
    print("RuleBot: Hello! I'm a rule-based chatbot. Type 'bye' or 'exit' to quit.")

    # Continuous loop
    while True:
        user_input = input("You: ")

        if not user_input.strip():
            print("RuleBot: Please type something.")
            continue

        response = get_response(user_input)
        print(f"RuleBot: {response}")

        if is_exit_command(user_input):
            break


if __name__ == "__main__":
    main()