import openai
import random

# Set up the OpenAI API key and GPT-3 engine
openai.api_key = "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"
engine = "davinci"

# Define the personalities and conversation styles
personalities = {
    "confident": "I know what I'm talking about.",
    "passionate": "I really care about this topic.",
    "calm": "Let's take a step back and think about this.",
    "empathetic": "I can understand where you're coming from.",
    "angry": "I'm getting really frustrated with this.",
    "impatient": "Can we please hurry this up?",
}

styles = {
    "dramatic": "This is such a huge deal!",
    "sarcastic": "Oh, joy.",
    "funny": "Ha ha, that's hilarious.",
    "laconic": "Meh.",
    "cowboy": "Howdy, partner!",
    "anime": "OwO what's this?",
}

# Define a function to generate a response based on the chosen personality and conversation style
def generate_response(prompt, personality, style, max_tokens=50):
    prompt += f" Personality: {personalities[personality]}. Style: {styles[style]}."
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
    )
    message = response.choices[0].text.strip()
    return message

# Define a function to handle user input and generate a response
def handle_input(prompt, personality, style):
    # Generate a response based on the user input and chosen personality and style
    message = generate_response(prompt, personality, style)
    return message

# Define a function to run the chatbot
def run_chatbot():
    print("Welcome to the chatbot!")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        else:
            personality = input("Choose a personality type: confident, passionate, calm, empathetic, angry, impatient: ")
            style = input("Choose a conversation style: dramatic, sarcastic, funny, laconic, cowboy, anime: ")
            message = handle_input(prompt, personality, style)
            print(f"Chatbot: {message}")

# Run the chatbot
run_chatbot()
