SPACE=" "
UNDER_SCORE = "_"
SLASH = "/"
BACK_SLASH = "\\"


def main():
    top()
    bottom()

    carriage_return()

    hashed_line()

    carriage_return()

    top()
    bottom()

    carriage_return()

    hashed_line()
    bottom()

    carriage_return()

    top()
    hashed_line()
    bottom()

def top():
    print (SPACE * 2, end="")
    print (UNDER_SCORE * 7,)
    print (SPACE, end="")
    print (SLASH, end="")
    print (SPACE * 7, end="")
    print (BACK_SLASH)
    print (SLASH, end="")
    print (SPACE * 9, end="")
    print (BACK_SLASH)

def bottom():
    print (BACK_SLASH, end="")
    print (SPACE * 9, end="")
    print (SLASH)
    print (SPACE, end="")
    print (BACK_SLASH, end="")
    print (UNDER_SCORE * 7, end="")
    print (SLASH) 

def hashed_line():
    print("-\"-'-\"-'-\"-")

def carriage_return():
    print ()  


main() 

