def main(age,citizen_yrs):
    print(eligible_for_house(age,citizen_yrs))
    print(eligible_for_senate(age, citizen_yrs))

def eligible_for_house(age,citizen_yrs):
    if age >= 25 and citizen_yrs >= 7:
        return True
    else:
        return False

def eligible_for_senate(age, citizen_yrs):
    if age >= 30 and citizen_yrs >= 9:
        return True
    else:
        return False

main(25, 7)