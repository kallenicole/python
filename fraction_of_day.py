def main():
    print('Time' + '         ' + 'Fraction Since Midnight')
    print('12:00 am' + '     ' + '0.0000')
    
    looping_around_the_clock()
    

def fraction_of_day(h,m,s,a_p):
    hour = 3600                                         #number of sec in an hour
    minute = 60                                         #number of sec in a minute
    sec = 1                     
    sec_in_day = 86400                                  #number of sec in a day
    seconds_result = (h * hour) + (m * minute) + (s * sec) 
    
    if a_p == 'p' and h < 12:                           #the "pm case": basically converts the hour to military time (except for noon)
        seconds_result = ((h + 12) * hour) + (m * minute) + (s * sec)
    elif h == 12 and a_p == 'a':                        #the "midnight case"
        seconds_result = (m * minute) + (s * sec)
    else:                                               #the "am case"
        seconds_result = (h * hour) + (m * minute) + (s * sec)      
    
    fraction_sec = seconds_result/sec_in_day
    return fraction_sec                                 #how many sec since zero hour of the time specified
                         


def looping_around_the_clock():
    for i in range(1,24):                               #loop around 23 times
        minute = 0
        second = 0 
        if i <= 11:
            am_or_pm = 'a'
            the_hour = i
        elif i == 12:
            the_hour = 12
            am_or_pm = 'p'
        else:
            am_or_pm = 'p'
            the_hour = i-12                             #if i = 13 for example, subtract 12 to make it 1 (pm)
        storing_var = fraction_of_day(the_hour, minute, second, am_or_pm)   #each time I loop, I'll store the fraction_of_day result
        
        print(f'{the_hour}:00 {am_or_pm}m', end="")
        if the_hour >= 10 and the_hour <= 12:
            print (f'{storing_var:11.4f}')
        else:
            print(f'{storing_var:12.4f}')
       
main()