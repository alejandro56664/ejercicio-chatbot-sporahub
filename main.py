from similarity import find_most_similar
from corpus import CORPUS

class Bot:

    def __init__(self):
        self.event_stack = []
        self.settings = {
            "min_score": 0.2
        }

        print("Hazme una pregunta:")
        while(True):
            self.allow_question()

    def allow_question(self):
        # Check for event stack
        potential_event = None
        if(len(self.event_stack)):
            potential_event = self.event_stack.pop()
        if potential_event:
            text = input("Pregunta: ")
            potential_event.handle_response(text, self)
        else:
            text = input("Respuesta: ")
            answer = self.pre_built_responses_or_none(text)
            if not answer:
                answer = find_most_similar(text)
                self.answer_question(answer, text)

    def answer_question(self, answer, text):
        if answer['score'] > self.settings['min_score']:
            # set off event asking if the response question is what they were looking for
            print("\nTal vez querías decir: %s (Score: %s)\nAnswer: %s\n" % (answer['question'],
                                                                          answer['score'],
                                                                          answer['answer']))
        else:
             print("No entiendo lo que me dices, mi habilidad es un poco limitada. Si te puede ayudar, he generado un link de google: \nhttps://www.google.com/search?q=%s\n" % ("+".join(text.split(" "))))
    

    def pre_built_responses_or_none(self, text):
        # only return answer if exact match is found
        pre_built = [
            {
                "Question": "hola",
                "Answer": "Hola, Soy un Chatbot de pruebas\n"
            },
            {
                "Question": "chao",
                "Answer": "Fue un placer ayudarte en tus preguntas!\n"
            }, 
            {
                "Question": "gracias",
                "Answer": "Es un placer ayudarte!\n"
            }
        ]
        for each_question in pre_built:
            if each_question['Question'].lower() in text.lower():
                print(each_question['Answer'])
                return each_question


    def dump_corpus(self):
        question_stack = []
        for each_item in CORPUS:
            question_stack.append(each_item['Question'])
        return question_stack
Bot()
