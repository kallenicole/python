## This is file choice_question.py
# This module defines a class that extends the base
# Question class.
#
from question import Question

## A ChoiceQuestion is a Question with multiple choices.
#
class NumericQuestion(Question) :

    # Constructor
    def __init__(self) :
        super().__init__()
        #self.check_numeric()

    def checkAnswer(self, response) :
        margin_error = 0.010000000000000009
        abs_response = abs(self._answer - response)
        if abs_response <= margin_error or response == self._answer:
            return True
        else:
            return False
        #return float(response) == float(self._answer)

    def present_question(q) :
        q.display() # Uses dynamic method lookup.
        response = float(input("Your answer: "))
        #print(f"{response} from numeric")
        #print(type(response))
        print(q.checkAnswer(response))

