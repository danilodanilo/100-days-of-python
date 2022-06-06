from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    question = Question(question_text, question_answer)
    question_bank.append(question)

is_on = True
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is: {quiz.score} out of {quiz.question_number}")