from question_model import Question
from data import question_data
from quiz_brain import QuizBank

question_bank = []
for quiz in question_data :
    question_bank.append(Question(quiz["question"], quiz["correct_answer"]))

quiz = QuizBank(question_bank)
while quiz.still_has_question() :
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
