from question import Question
from data import question_data
from quizBrain import QuizBrain

# We will loop through the question in data and append them in question bank through Question class
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your score is {quiz.score}/{quiz.question_number}")