def change():
    difference = 0
    max_difference = 0
    n1 = int(input("Enter a stock price: "))        #the initial input to start off the days
    day = 0

    for i in range(9):                              #only loop 9 times because we have already asked for 1 input
        n2 = int(input("Enter a stock price: "))
        difference = abs(n1 - n2)
        n1 = n2

        if difference > max_difference:
             max_difference = difference
             day = i                        #if difference is updating the new max_difference, also reassign the "day" variable to i
                                            #print(difference) will show the difference from day to day

    #have to increase day by 1 because we have input one day out of the loop .
    print (f'The largest change of {max_difference} occured between day #{day+1} and #{day+2}')

change()


