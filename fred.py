""" def main():
    concentration = "fred"
    fred = "computer science"
    computer = "department"
    department = "student"
    student = "concentration"
    
    sentence(student, "fred", concentration)
    sentence(fred, computer, department)    

def sentence(x, y, z):
    print("Many a " + z + " in the "
    + y + " of " + x)

main()  """

def main():
    concentration = "fred"
    fred = "computer science"
    computer = "department"
    department = "student"
    student = "concentration"

    sentence(student, "fred", concentration)
    sentence(fred, computer, department)

def sentence(concentration, fred, foo):
    print("Many a " + foo + " in the "
    + fred + " of " + concentration)

main() 