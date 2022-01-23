def vowel_count(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = []
    for i in range(0,5):
        the_count = s.count(vowels[i])
        counter.append(the_count)
    return counter

print(vowel_count("a eeeee iii oo uuuuuu"))