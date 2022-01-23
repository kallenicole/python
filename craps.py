import random

def main():
    play_second_round()

def do_roll():                              #roll two dice and sum their values
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    return [die1, die2]

def play_first_round():                         
    two_die_values = do_roll()                                  #roll the dice
    sum_of_roll = two_die_values[0] + two_die_values[1]         #set sum of the roll to the sum of the dice roll
    answer = [4, 5, 6, 8, 9, 10]                                #these are the values we are looiking for
    while sum_of_roll not in answer:                            #while the sum of the roll isnt what we are looking for, roll again
        print(f'Computer rolls a {two_die_values[0]} and a {two_die_values[1]} for a total of {sum_of_roll}')
        do_roll()
        two_die_values = do_roll()                              #set sum of the roll to the sum of the dice roll   
        sum_of_roll = two_die_values[0] + two_die_values[1]
    players_point = sum_of_roll                                 #when we get one of the lucky numbers in "answer", assign the player's point 
    print(f'Computer rolls a {two_die_values[0]} and a {two_die_values[1]} for a total of {players_point}')
    print(f'{players_point} is now the established POINT.')
    return players_point

def play_second_round():
    players_point = play_first_round()                          #call the first round play function
    two_die_values = do_roll()                               
    sum_of_roll = two_die_values[0] + two_die_values[1]         #set sum of the roll to the sum of the dice roll
    while sum_of_roll != 7 and sum_of_roll != players_point:    #roll again if two dice dont equal 7 or the players point
        print(f'Computer rolls a {two_die_values[0]} and a {two_die_values[1]} for a total of {sum_of_roll}')
        do_roll()
        two_die_values = do_roll()                              #set sum of the roll to the sum of the dice roll   
        sum_of_roll = two_die_values[0] + two_die_values[1]
    print(f'Computer rolls a {two_die_values[0]} and a {two_die_values[1]} for a total of {sum_of_roll}')
    if sum_of_roll == 7:                                        #checking for the roll equaling 7 or the players point
        print('You lose!')
    elif sum_of_roll == players_point:
        print('You win!')

main()