import random

def compare_two():
    num1 = random.randint(1,7)
    num2 = random.randint(1,7)
    if num1 == num2:
        print (f'We drew {num1} and {num2}, a tie!')
    elif abs(num1 - num2) % 2 == 0:
        print (f'We drew {num1} and {num2}, so you win!')
    else:
        print (f'We drew {num1} and {num2}, so you lose!')

compare_two()