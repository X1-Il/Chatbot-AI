import openai

# Set up OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

# Function to generate a chatbot response
def generate_response(user_input):
    prompt = f'Title: {title}\nDescription: {description}\nUser: {user_input}\nBot:'
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10
    )
    return response.choices[0].text.strip()

# Run the chatbot
while True:
    user_input = input("User: ")
    if user_input.lower() == 'quit':
        break
    response = generate_response(user_input)
    print("Bot:", response)
