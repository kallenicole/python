def donor():
    donation = int(input("Enter a donation amount: "))
    if donation > 0:
        if donation >= 10000:
            print("Benefactor")
        elif donation < 10000 and donation >= 1000:
            print ("Patron")
        elif donation < 1000 and donation >= 200:
            print ("Supporter")
        elif donation < 200 and donation >= 15:
            print ("Friend")
        else:
            print ("Cheapskate")
    else:
        print("You cannot enter a negative donation.")


donor()