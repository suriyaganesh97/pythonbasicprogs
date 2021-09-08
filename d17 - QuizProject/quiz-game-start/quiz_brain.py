class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        correct_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q{self.question_number} {current_question.text} (True/False) : ")
        self.check_answer(correct_answer,user_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,correct_answer,user_answer):
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print("you got it right")
        else:
            print("your answer is wrong")

        print(f"the correct answer is {correct_answer}")
        print(f"your score is {self.score} / {self.question_number}")



