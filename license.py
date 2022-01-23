import random
import string

def main(): 
    twenty_license_plates()
   
def twenty_license_plates():
    for nums_and_letters in range (1,21):       #loop twenty times and print a random license plate each time
        nums_and_letters = license_plate()
        print("".join(nums_and_letters))

def license_plate():
    license = []
    for i in range(1,4):
        i = random.choice(string.ascii_uppercase)           #loop 3 times and assign random uppercase letters
        license.append(i)
    license.append(" ")
    for k in range(1,4):
        k = str(random.randint(1,9))
        license.append(k)
    return license

main()