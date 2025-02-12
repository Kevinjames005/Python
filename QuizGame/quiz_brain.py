class QuizBank:
    def __init__(self , q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} , (Ture\\False) :")
        self.check_answer(user_answer, current_question.answer)
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

    def check_answer(self,user_answer,question_answer):
        if user_answer.lower()== question_answer.lower():
            print("You got it.")
            self.score += 1
        else :
            print("That's wrong.")
            print(f"The correct answer was {question_answer}")