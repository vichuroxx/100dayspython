from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions()==True:
    quiz.next_question()
