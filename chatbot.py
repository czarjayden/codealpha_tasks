import nltk
from nltk.chat.util import Chat, reflections

# Predefined patterns and responses
pairs = [
    (r"hello|hi|hey", ["Hello there!", "Hi, how can I help you?"]),
    (r"how are you ?", ["I'm mighty good. What about you?"]),
    (r"(.*) your name ?", ["My name is Chatbot! What's yours?"]),
    (r"quit", ["Goodbye! It was nice chatting with you."]),
    (r"(.*)", ["I'm not sure I understand. Can you elaborate?"])
]

# Initialize chatbot with patterns
chatbot = Chat(pairs, reflections)

# Start conversation
def start_chatbot():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chatbot()