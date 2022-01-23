#password rules
#password >= 8 characters
#password.isupper() >= 1
#password.islower() >= 1
#password.isdigit() >= 1


def password():
    password = input("Type a password according to the rules: ")
    valid = is_valid(password)
    print(valid)
    while valid == False:
        print("Invalid password, try again.")
        password = input("Type a password according to the rules: ")
        valid = is_valid(password)
    while valid == True:
        password1 = input("Now type your password again: ")
        if password == password1:
            print("Success")
            break
        else:
            print("Passwords don't match.")
            password1 = input("Type your password again:")
    

def is_valid(pwd):
    if len(pwd) < 8:
        return False
    if not any(char.isupper() for char in pwd):
        return False
    if not any(char.islower() for char in pwd):
        return False
    if not any(char.isdigit() for char in pwd):
        return False
    return True

password()