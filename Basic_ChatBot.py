''''
2)Basic Chatbot
Create a text-based chatbot that can have
conversations with users. You can use natural
language processing libraries like NLTK or spaCy to
make your chatbot more conversational.
'''




import nltk
from nltk.chat.util import Chat, reflections
import random


pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there! How can I assist you today?", "Hey! How are you doing?"]
    ],
    [
        r"how are you ?",
        ["I'm doing great! How about you?", "I'm fine, thank you! What about you?"]
    ],
    [
        r"what is your name ?",
        ["I'm your virtual assistant. You can call me ChatBot.", "I’m a chatbot built to assist you."]
    ],
    [
        r"my name is (.*)",
        ["Nice to meet you, %1! How can I assist you today?", "Hello %1! What would you like to talk about?"]
    ],
    [
        r"what can you do ?|how can you help me ?",
        ["I can chat with you, answer your questions, and help you with basic tasks.",
         "I can help you with programming questions, general knowledge, and basic tasks."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!",
         "Why did the scarecrow win an award? Because he was outstanding in his field!"]
    ],
    [
        r"bye|goodbye|exit",
        ["Goodbye! Have a great day!", "Bye! Take care. Hope to talk to you soon."]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem! I'm here to help.", "Anytime!"]
    ],
    [
        r"(.*)weather(.*)",
        ["I'm not connected to real-time data, but you can check weather updates on your local app.",
         "Sorry, I don't have weather information, but try using a weather app."]
    ],
    [
        r"(.*)your favorite (.*)",
        ["I don't have favorites, but I love helping people!", "I'm a fan of anything that involves learning."]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Could you ask something else?",
         "Interesting question! Can you clarify?",
         "Sorry, I don't understand that. Try asking something different."]
    ]
]


def chatbot():
    print("Hi, I'm your interactive chatbot! Type 'bye' to exit the chat.")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    chatbot()
