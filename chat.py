import openai

# Set up your OpenAI API key
openai.api_key = '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'

# Function to ask the chatbot a question and get a response
def ask_chatbot(question, chat_log=[]):
    # Append user's question to the chat log
    chat_log.append(question)

    # Generate a response from OpenAI API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt='\n'.join(chat_log),
        temperature=0.7,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    # Retrieve and return the chatbot's reply
    reply = response.choices[0].text.strip()
    chat_log.append(reply)
    return reply

# Main loop
chat_log = []

while True:
    user_input = input("User: ")

    # Check if the user wants to exit
    if user_input.lower() == "exit":
        break

    # Get a response from the chatbot
    bot_response = ask_chatbot(user_input, chat_log)
    print("Chatbot:", bot_response)

