import random
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.listOfNumbers = []

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):

        # This will ensure that question will be taken randomly
        questionNumber = random.randint(0, len(self.question_list)) - 1
        # This will ensure that any question will not be repeat
        for number in self.listOfNumbers:
            if number == questionNumber:
                questionNumber = random.randint(0, len(self.question_list)) - 1

        current_question = self.question_list[questionNumber]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number} : {current_question.text} (True/False) : ")
        
        self.check_answer(user_answer, current_question.answer)
        self.listOfNumbers.append(questionNumber)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("That was right")
            self.score += 1
        else:
            print("That's was wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")