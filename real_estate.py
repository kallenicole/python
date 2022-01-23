def modified(ad):
    new_ad = []
    split_ad = [char for char in ad]            #split the ad entered into characters.
    new_ad.append(split_ad[0])                  #append the first letter to the new list.
    for char in range (1, len(split_ad)):       #loop through the characters and 
        if is_vowel(split_ad[char]) == False:   #if is_vowel is False 
            new_ad.append((split_ad[char]))     #append the character to the new ad.   
    return "".join(new_ad)                      #join the characters together.              
        
def is_vowel(c):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  #function to check if characters are vowels. 
    if c in vowel:
        return True
    else:
        return False

print(modified("One block from Harvard square, beautiful furnished flat with gorgeous garden."))