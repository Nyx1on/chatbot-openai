import openai
import random

# Set up the OpenAI API key and GPT-3 engine
openai.api_key = "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"
engine = "davinci"

# Define the personalities and conversation styles
personalities = {
    "confident": "confident",
    "passionate": "passionate",
    "calm": "calm",
    "empathetic": "empathetic",
    "angry": "angry",
    "impatient": "impatient",
}

styles = {
    "dramatic": "dramatic",
    "sarcastic": "sarcastic",
    "funny": "funny",
    "laconic": "laconic",
    "cowboy": "cowboy",
    "anime": "anime",
}

# Define a function to generate a response based on the chosen personality and conversation style


def generate_response(prompt, personality, style, max_tokens=50):
    prompt += f"reply with personality: {personalities[personality]} and style: {styles[style]}."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    message = response.choices[0].message.content
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
            personality = input(
                "Choose a personality type: confident, passionate, calm, empathetic, angry, impatient: ")
            style = input(
                "Choose a conversation style: dramatic, sarcastic, funny, laconic, cowboy, anime: ")
            message = handle_input(prompt, personality, style)
            print(f"Chatbot: {message}")


# Run the chatbot
run_chatbot()
