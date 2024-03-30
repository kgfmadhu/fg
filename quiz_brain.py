class QuizBrain:
    def __init__(self,question_list):
        self.question_no=0
        self.question_list=question_list
        self.score=0
    
    def nextquestion(self):
        current_question=self.question_list[self.question_no]
        self.question_no+=1
        result=input(f"Q:{self.question_no} {current_question.text} (True/False):")
        if result.lower()==current_question.answer.lower():
            self.score+=1
            print(f"score is{self.score}/{self.question_no}")
        else:
            print("ur answer is wrong")
        print(f"The answer is{current_question.answer}")
        

    def still_has_questions(self):
        return self.question_no<len(self.question_list)