def main():
    month = int(input("Enter your birth month number: "))                           #asking for user input
    day = int(input("Enter the date of your birth: "))
    print(sign(month,day))

def valid_date(month, day):
    if month > 12 or month < 0:                                                     #month greater than 12 or negative
        return False

    if day < 0:                                                                     #negative days
        return False

    if (month == 4 or month == 6 or month == 9 or month == 11 and day <= 30):       #30-day months
        return True

    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and day <= 31):  #31-day months
        return True

    if  (month == 2 and day >= 29):                                                  #February case
        return False
   


def sign (month, day): 
    your_sign = ""
    if valid_date(month, day) == False:
        print ("Invalid Date")
    elif month == 3:
        if day >= 21:
            your_sign = "Aries"
        else:
            your_sign = "Pisces"
    elif month == 4:
        if day >= 20:
            your_sign = "Taurus"
        else:
            your_sign = "Aries"
    elif month == 5:
        if day >= 21:
            your_sign = "Gemini"
        else:
            your_sign = "Taurus"
    elif month == 6:
        if day >= 21:
            your_sign = "Cancer"
        else:
            your_sign = "Gemini"
    elif month == 7:
        if day >= 23:
            your_sign = "Leo"
        else:
            your_sign = "Cancer"
    elif month == 8:
        if day >= 23:
            your_sign = "Virgo"
        else:
            your_sign = "Leo"
    elif month == 9:
        if day >= 23:
            your_sign = "Libra"
        else:
            your_sign = "Virgo"
    elif month == 10:
        if day >= 23:
            your_sign = "Scorpio"
        else:
            your_sign = "Libra"
    elif month == 11:
        if day >= 22:
            your_sign = "Sagittarius"
        else:
            your_sign = "Scorpio"
    elif month == 12:
        if day >= 22:
            your_sign = "Capricorn"
        else:
            your_sign = "Sagittarius"
    elif month == 1:
        if day >= 20:
            your_sign = "Aquarius"
        else:
            your_sign = "Capricorn"
    elif month == 2:
        if day >= 19:
            your_sign = "Pisces"
        else:
            your_sign = "Aquarius"
    
    return your_sign

main()
