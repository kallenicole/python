## This is file choice_question.py
# This module defines a class that extends the base
# Question class.
from question import Question

## A ChoiceQuestion is a Question with multiple choices.
class ChoiceQuestion(Question) :
    # Constructs a choice question with no choices.
    def __init__(self) :
        super().__init__()
        self._choices = []

    # define everything else that's needed
    def add_choice(self, country, truthy):
        self._choices += [[country, truthy]]
        self.choice_set_answer()

    def choice_set_answer(self):
        for i, val in enumerate(self._choices):
            # to account for starting list from the number 1 and not 0
            i+=1
            if val[1] == True:
                self._answer = (str(i))

    def checkAnswer(self, response) :
        return response == self._answer

    def display(self):
        print(self._text)
        for i, val in enumerate(self._choices):
            # to account for starting list from the number 1 and not 0
            i+=1
            print(f"{i}: {val[0]}")
       

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

