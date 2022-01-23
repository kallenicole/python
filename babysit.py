HOURLY_RATE_REG = 5.5
HOURLY_RATE_EXTRA = 8
HOURLY_RATE_SUPER_LATE = 10

def main():
    time_conversion()

def time_conversion():
    hour_starting = int(input("What hour did the babysitter start? "))
    min_starting = int(input("What minute did the babysitter start? "))
    hour_stopping = int(input("What hour did the babysitter end? "))
    min_stopping = int(input("What minute did the babysitter end? "))
       

    if hour_stopping >= 6 and hour_stopping <= 12:                  
        converted_hour_stopping = hour_stopping
    else:
        converted_hour_stopping = hour_stopping + 12                        #converting the early AM hours to a "reverse military time"

    if is_entry_valid(hour_starting, min_starting, converted_hour_stopping, min_stopping) == False:
        print ("Enter a valid time.")
        return 

    sum1 = (how_many_hours_at_what_rate(hour_starting, converted_hour_stopping))
    sum2 = (how_many_min_at_what_rate(hour_starting, min_starting, converted_hour_stopping, min_stopping))

    print(f'The paycheck is ${sum1 + sum2:0.2f}') 


def is_entry_valid(hour_starting, min_starting, hour_stopping, min_stopping):
    if hour_starting < 6 or hour_starting > 11:
        return False
    if hour_stopping < 9 or hour_stopping > 16:
        return False
    elif min_starting < 0 or min_starting > 59:
        return False
    elif min_stopping < 0 or min_stopping > 59:
        return False
    elif hour_stopping < hour_starting:                     #invalid if the stop hour is before the start hour
        return False


def how_many_hours_at_what_rate(start_hour,end_hour):
    number_hours_super_late = 0
    number_hours_extra = 0
    number_hours_reg = 0

    if end_hour > 12: 
        number_hours_super_late = end_hour - 12
        number_hours_extra = 12 - 8
        number_hours_reg = 8 - start_hour

    elif end_hour <= 12 and end_hour > 8: 
        number_hours_extra = end_hour - 8
        number_hours_reg = 8 - start_hour
    
    else:    
        end_hour <= 8
        number_hours_reg = end_hour - start_hour
    
    the_hour_sum = ((HOURLY_RATE_EXTRA * number_hours_extra) + (HOURLY_RATE_REG * number_hours_reg) + (HOURLY_RATE_SUPER_LATE * number_hours_super_late))
    return the_hour_sum
    

def how_many_min_at_what_rate(start_hour, min_starting, stop_hour, min_stopping):

    if start_hour <= 8 and start_hour >= 6:
        start_min_calc = abs(0 - min_starting) * (HOURLY_RATE_REG / 60)             #starting between 6-8PM
    else:
        start_min_calc = abs(0 - min_starting) * (HOURLY_RATE_EXTRA / 60)           #starting between 8-11PM

    if stop_hour > 12:
        stop_min_calc = abs(0 - min_stopping) * (HOURLY_RATE_SUPER_LATE / 60)       #stopping between 12-4AM
    else: 
        stop_min_calc = abs(0 - min_stopping) * (HOURLY_RATE_EXTRA / 60)            #stopping between 9-12AM

    the_min_sum = (start_min_calc + stop_min_calc)
    return the_min_sum
    

main()


