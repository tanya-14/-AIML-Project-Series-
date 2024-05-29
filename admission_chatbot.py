class AdmissionChatbot:
    def __init__(self):
        self.user_data = {}

    def greeting(self):
        return "Welcome to the College Admission Helpdesk! How can I assist you today?"

    def farewell(self):
        return "Goodbye! Feel free to reach out if you have more questions."

    def admission_responses(self, user_input):
        responses = {
            "how do i apply?": "You can apply through our online portal on the college website.",
            "what are the admission requirements?": "You need a minimum GPA of 3.0, SAT/ACT scores, and two recommendation letters.",
            "when is the application deadline?": "The application deadline is December 15th.",
            "what documents are required?": "You need to submit your transcripts, test scores, and recommendation letters.",
            "can i get a scholarship?": "Yes, there are several scholarships available based on merit and need."
        }
        return responses.get(user_input.lower(), "I'm sorry, I didn't understand that. Can you please rephrase?")

    def remember_interaction(self, user_name, key, value):
        if user_name not in self.user_data:
            self.user_data[user_name] = {}
        self.user_data[user_name][key] = value

    def recall_interaction(self, user_name, key):
        return self.user_data.get(user_name, {}).get(key, None)

    def ask_questions(self):
        questions = ["What's your name?", "What course are you interested in?", "Do you have any specific questions about the admissions process?"]
        responses = []
        for question in questions:
            user_input = input(question + " ")
            responses.append(user_input)
        return responses

    def handle_interaction(self):
        print(self.greeting())
        user_name = input("What's your name? ")
        self.remember_interaction(user_name, "name", user_name)

        course_interest = input("What course are you interested in? ")
        self.remember_interaction(user_name, "course_interest", course_interest)

        specific_questions = input("Do you have any specific questions about the admissions process? ")
        self.remember_interaction(user_name, "specific_questions", specific_questions)

        print(f"Nice to meet you, {user_name}. I'll try to help you with information about {course_interest} admissions.")

        while True:
            user_input = input("Ask me an admission-related question or type 'bye' to end the chat: ")
            if user_input.lower() == 'bye':
                print(self.farewell())
                break
            else:
                print(self.admission_responses(user_input))

if __name__ == "__main__":
    chatbot = AdmissionChatbot()
    chatbot.handle_interaction()
