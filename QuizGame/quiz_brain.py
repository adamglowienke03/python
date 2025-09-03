class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.correct_answer = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (true/false): ").lower()
        if user_answer == current_question.answer.lower():
            self.correct_answer += 1
            print(f"Your score: {self.correct_answer}/{self.question_number}")
        else:
            print(f"Your score: {self.correct_answer}/{self.question_number}")
        print("\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)