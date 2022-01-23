def guess():
    print("This program has you, the user, choose a number between 1 and 100.")
    print("Then I, the computer, will try my best to guess it.")
    print("If I guess a number that is SMALLER than the secret number, type s.")
    print("If I guess a number that is BIGGER than the secret number, type b.")
    print("And if I guess correctly, type c.")
    #initialize the guess, the ceiling (100) and the floor(1). 
    new_guess = 0
    ceiling = 101
    floor = 1
    #initialize a "response" so it goes into the while loop
    response = 's'

    while response != 'c':
        #next s or b operation needs to take the new guess and divide by 2 to guess in the middle
        new_guess = int(abs(ceiling - floor) / 2 + floor)
        response = input(f'Is it {new_guess}? (Type s, b, or c) ')
        #reset new floor or reset new ceiling
        if response == 's':
            floor = new_guess
        elif response == 'b':
            ceiling = new_guess
        elif response == 'c':
            print('Correct!')
        else:
            print('Please enter a valid key.')  

guess()