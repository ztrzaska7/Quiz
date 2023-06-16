import random
#klasa pytanie
class Question:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer
#klasa quiz
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
    def run(self):
        random.shuffle(self.questions)
        for question in self.questions:
            print(question.question)
            user_answer=input("Put Your answer: ")
            if user_answer.lower()==question.answer.lower():
                self.score+=1
                print("The answer is correct")
            else:
                print("The answer is incorrect")
        self.display_score()
    def display_score(self):
        total_question=len(self.questions)
        print(f"Your result is: {self.score}")
        print(f"You have answered correctly for {self.score} for {total_question} questions")
#przykłady
question1=Question("What is a capital of Poland?","Warszawa")
question2=Question("What is a capital of Germany?","Berlin")
quiz=Quiz([question1,question2])

quiz.run()


#jak działa quiz:
# musimy dodać pytania
# dodać odpowiedzi
# losować w jakiej kolejności będą się pojawiały pytania
# musi być miejsce na dodanie odpowiedzi
# zliczać czy dobrze odpowiedzieliśmy
# co zawiera quiz: pytania, zbieranie punktow