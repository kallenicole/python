def main():
    return is_palindrome("Murder for a jar of red rum"), is_palindrome("Madam"), is_palindrome("Hello")

def is_palindrome(a_string):
    lower_string = a_string.lower()
    clean_string = lower_string.replace(" ", "")
    if len(clean_string) <= 1:
         return True
    elif clean_string[0] == clean_string[-1]:
        return is_palindrome(clean_string[1:len(clean_string)-1])
    else:
        return False


print(main())