def main():
    return index_of("Mississippi", "QmIss"), index_of("Nebraska", "neb")


def index_of(text, a_string):
    if len(text) < len(a_string):
        return -1
    #if the text from pos 0 - length of the string = the string, we are done
    elif text[0:len(a_string)].lower() == a_string.lower():
        return 0
    else:
        break_down = index_of(text[1:].lower(), a_string.lower())
        if break_down == -1:
            return -1
        else:
            return break_down + 1

print(main())