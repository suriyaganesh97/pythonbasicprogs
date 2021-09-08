from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []  # creating a empty list
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    question_obj = Question(question_text, question_answer) # creating question_obj objects for all questions
    question_bank.append(question_obj)   #creating a list of all ques objects

quizBrain = QuizBrain(question_bank)

while quizBrain.still_has_questions():
    quizBrain.next_question()

print("you have completed the quiz!!")
print(f"your final score is {quizBrain.score}")




# question_bank = Question("text", "answer")
