##
# This program shows a simple quiz with 2 question types.
#
from question import Question
from choice_question import ChoiceQuestion
from numeric_question import NumericQuestion


def main():
    first = Question()
    first.set_text("Who was the inventor of Python?")
    first.set_answer("Guido van Rossum")
    present_question(first)

    second = ChoiceQuestion()
    second.set_text("Where was the inventor of Python born?")
    second.add_choice("Australia", False) 
    second.add_choice("Canada", False) 
    second.add_choice("Netherlands", True) 
    second.add_choice("United States", False) 
    second.choice_set_answer()
    present_question(second)

    third = NumericQuestion()
    third.set_text("What is 3/4 (expressed as a decimal)?")
    third.set_answer(0.75)
    third.present_question()

## Presents a question to the user and checks the response.
# @param q the question
#
def present_question(q) :
    q.display() # Uses dynamic method lookup.
    response = input("Your answer: ")
    print(q.checkAnswer(response))

# Start the program.
main()