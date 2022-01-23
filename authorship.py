# open and read a file
data = input("What file would you like to open? ")
with open(data) as file:
    data = file.read()
    file.close()

def main():
    remove_char(data)

def remove_char(the_text):
    counter = {'1-letter':0, '2-letter':0, '3-letter':0, '4-letter':0, '5-letter':0,
    '6-letter':0, '7-letter':0, '8-letter':0, '9-letter':0, '10-letter':0,
    '11-letter':0, '12-letter':0, '13-(or more) letter':0}
    total = 0        #",.!?;:][-\""
    special_char = [",", ".", "!", "?", ";", ":", "]", "\\", "[", "-", '"']
    #remove special characters and split into list of words
    #the_text = ''.join(i for i in the_text if not i in special_char)
    the_text = the_text.replace("'", "")
    for char in special_char:
        the_text = the_text.replace(char, " ")
    #print(the_text)
    split_list = the_text.split()
    #print(split_list)
    # iterate through the list of words and append the number of characters to a dictionary of word_nums and their counts (keys)
    for i in range (len(split_list)):
        #find total number of words
        total += 1
        for key in counter:
            if i < 13:
                counter[key] = counter[key] + 1
            else: 
                counter[key] = counter[key] + 1
        print(counter)
        # for values in counter:
        #     if i < 13:
        #         values += 1
        #     else:
        #         values += 1
        # if len(split_list[i]) == 1:
        #     counter['1-letter'] += 1
        # elif len(split_list[i]) == 2:
        #     counter['2-letter'] += 1
        # elif len(split_list[i]) == 3:
        #     counter['3-letter'] += 1
        # elif len(split_list[i]) == 4:
        #     counter['4-letter'] += 1
        # elif len(split_list[i]) == 5:
        #     counter['5-letter'] += 1
        # elif len(split_list[i]) == 6:
        #     counter['6-letter'] += 1
        # elif len(split_list[i]) == 7:
        #     counter['7-letter'] += 1
        # elif len(split_list[i]) == 8:
        #     counter['8-letter'] += 1
        # elif len(split_list[i]) == 9:
        #     counter['9-letter'] += 1
        # elif len(split_list[i]) == 10:
        #     counter['10-letter'] += 1
        # elif len(split_list[i]) == 11:
        #     counter['11-letter'] += 1
        # elif len(split_list[i]) == 12:
        #     counter['12-letter'] += 1
        # elif len(split_list[i]) >= 13:
        #     counter['13-(or more) letter'] += 1
    #print(total)
    #print the dictionary items with counts and their percentages to total
    for k in counter.keys():
        print(f'Proportion of {k} words: {counter[k] / total * 100:.1f}% ({counter[k]}) words.')
    
main()

