import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 

# Responses
responses = {
    "hi": "Hello! How can I assist you today?",
    "how are you": "I'm just a bot, but thanks for asking!",
    "bye": "Goodbye! Have a great day!",
}

# Function to process user input and return response
def respond(user_input):
    # Tokenize user input
    tokens = word_tokenize(user_input.lower())
    
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords.words('english')]

    # Check for matching tokens in responses
    matched_response = [responses[token] for token in tokens if token in responses]
    
    if matched_response:
        return matched_response[0]  # Return the first matched response
    else:
        return "Sorry, I didn't understand that. Can you please retry it?"

# Main loop for user interaction
while True:
    user_input = input("You: ")
    
    # Check for empty input
    if not user_input.strip():
        print("Please enter something.")
        continue

    response = respond(user_input)
    print("Bot:", response)
