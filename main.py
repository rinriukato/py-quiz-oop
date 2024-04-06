from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = item['question']
    answer = item['correct_answer']
    question_bank.append(Question(question, answer))

qb = QuizBrain(question_bank)

while qb.still_has_questions():
    qb.next_question()

print("You've completed the quiz")
print(f"Your final score was: {qb.score}/{qb.question_number}")