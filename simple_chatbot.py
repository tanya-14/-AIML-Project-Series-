import random

class SimpleChatbot:
    def __init__(self):
        self.user_data = {}

    def greeting(self):
        return "Hello! How can I help you today?"

    def farewell(self):
        return "Goodbye! Have a great day!"

    def basic_responses(self, user_input):
        responses = {
            "what's your name?": "I'm a simple chatbot created to assist you.",
            "how are you?": "I'm just a bunch of code, but thanks for asking!",
            "what can you do?": "I can chat with you and remember some basic information.",
            "who created you?": "I was created by a team of developers.",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!"
        }
        return responses.get(user_input.lower(), "I'm sorry, I didn't understand that. Can you please rephrase?")

    def remember_interaction(self, user_name, key, value):
        if user_name not in self.user_data:
            self.user_data[user_name] = {}
        self.user_data[user_name][key] = value

    def recall_interaction(self, user_name, key):
        return self.user_data.get(user_name, {}).get(key, None)

    def ask_questions(self):
        questions = ["What's your name?", "What's your favorite color?", "What do you like to do for fun?"]
        responses = []
        for question in questions:
            user_input = input(question + " ")
            responses.append(user_input)
        return responses

    def handle_interaction(self):
        print(self.greeting())
        user_name = input("What's your name? ")
        self.remember_interaction(user_name, "name", user_name)

        user_fav_color = input("What's your favorite color? ")
        self.remember_interaction(user_name, "favorite_color", user_fav_color)

        user_hobby = input("What do you like to do for fun? ")
        self.remember_interaction(user_name, "hobby", user_hobby)

        print(f"Nice to meet you, {user_name}! It's cool that you like {user_fav_color} and enjoy {user_hobby}.")

        while True:
            user_input = input("Ask me something or type 'bye' to end the chat: ")
            if user_input.lower() == 'bye':
                print(self.farewell())
                break
            else:
                print(self.basic_responses(user_input))

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.handle_interaction()
