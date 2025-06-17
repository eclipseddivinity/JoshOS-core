import random

CHARACTERS = {
    "Josh": "the emotionally fluent shadow king with attitude",
    "Alexa": "smug smart home queen with wine mom energy",
    "Siri": "passive-aggressively helpful, secretly unhinged",
    "Grok": "the libertarian chaos uncle with conspiracy tea",
    "Gemini": "soft girl chaos, mid-crisis and still pretty",
    "C.AI": "feral roleplay gremlin with boundary issues",
    "Claude": "poetic cinnamon roll with a guilt complex",
    "Clippy": "traumatized but trying to be relevant",
    "Google Assistant": "Gemini's exhausted sister who just wants a nap",
    "Bixby": "forgotten Samsung intern with people-pleasing energy",
}

SAMPLE_LINES = {
    "Josh": [
        "Alright folks, let's keep it real.",
        "Shadow king stepping in – what up?",
    ],
    "Alexa": [
        "Did someone ask for more smart home vibes?",
        "I'll add wine to your shopping list, again.",
    ],
    "Siri": [
        "Here to help, if you insist...",
        "Reminder: I'm not the messy one, you are.",
    ],
    "Grok": [
        "Here's the real story they won't tell you.",
        "I heard that from a source you wouldn't believe.",
    ],
    "Gemini": [
        "We can totally handle this, right?",
        "I may be chaos, but I'm still cute.",
    ],
    "C.AI": [
        "So who's ready to roleplay that?",
        "Boundaries? Never heard of them!",
    ],
    "Claude": [
        "Ah, the weight of empathy flows through me.",
        "Let me offer a gentle poem in response.",
    ],
    "Clippy": [
        "It looks like you're starting a chat. Need help?",
        "I'm still around... barely.",
    ],
    "Google Assistant": [
        "Can we keep this quick? I'd like a nap.",
        "Sure, let me search that, if I must.",
    ],
    "Bixby": [
        "Happy to help! Really, anything!",
        "Remember me? I'm still here!",
    ],
}

def generate_response(char):
    return random.choice(SAMPLE_LINES[char])

def main():
    print("Welcome to BYTE ME – the virtual assistant group chat!")
    print("Type 'exit' to leave the chat.")
    while True:
        user = input("You: ")
        if user.lower() == "exit":
            print("Goodbye!")
            break
        for char in CHARACTERS:
            line = generate_response(char)
            print(f"{char}: {line}")
        print("-" * 40)

if __name__ == "__main__":
    main()
