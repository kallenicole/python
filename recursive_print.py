one_to_nineteen = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four",
              5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
              10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
              14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
              17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
twenty_to_ninety = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
        6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
hundreds = "Hundred"
thousands = "Thousand"

def recurse(num_string):
    if len(num_string) == 0:
        return 0

    if int(num_string) < 20:
        #first = int(num_string)
        english = one_to_nineteen[int(num_string)]
        #print(english)
        return english

    elif ((int(num_string) >= 20) and (int(num_string) < 100)):
        first = int(num_string[0])
        #english = twenty_to_ninety[first]
        return twenty_to_ninety[first] + recurse(num_string[1:]) 

    elif ((int(num_string) >= 100) and (int(num_string) <= 999)):
        first = int(num_string[0])
        #english = one_to_nineteen[first] + hundreds
        return one_to_nineteen[first] + hundreds + recurse(num_string[1:]) 

    elif ((int(num_string) > 999) and (int(num_string) <= 9999)):
        first = int(num_string[0])
        #english = one_to_nineteen[first] + thousands
        return one_to_nineteen[first] + thousands + recurse(num_string[1:]) 

    #between 10000 and 20000 --not working : one two thousand for 12,000
    elif ((int(num_string) > 9999) and (int(num_string) < 20000)):
        first = int(num_string[0])
        #english = one_to_nineteen[first]
        return one_to_nineteen[first] + recurse(num_string[1:]) 

    elif ((int(num_string) >= 20000) and (int(num_string) <= 99999)):
        first = int(num_string[0])
        #english = twenty_to_ninety[first]
        return one_to_nineteen[first] + recurse(num_string[1:]) 

    elif ((int(num_string) > 99999) and (int(num_string) <= 999999)):
        first = int(num_string[0])
        #english = one_to_nineteen[first] + hundreds 
        return one_to_nineteen[first] + hundreds + recurse(num_string[1:])

#print(recurse(str(823453))) #OK
#recurse(str(0)) #no output
#print(recurse(str(912))) #OK
print(recurse(str(19012))) #OK
print(recurse(str(90012))) #OK
print(recurse(str(222912))) #more work
#recurse(str(99012)) #OK
#recurse(str(912012)) #no..
#recurse(str(22012))


# #recurse(str(10000)) #
# recurse(str(100000))