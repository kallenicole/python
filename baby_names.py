import string
import sys

def main():
    y = int(input("Please enter your decade: "))
    decade = translate_year(y)
    if decade == 0:
        print('Enter a valid date.')
        return
    lst = get_file_data_in_list_form()
    print(find_top_names(lst, decade))
    get_name_from_user(lst)
   
#get file data, load into a list, change numbers to ints
def get_file_data_in_list_form():
    name_list = []
    with open("test_names.txt", "r") as f:
        for line in f:
            line = line.split()
            name_list.append(line) 
        for i in range(0, len(name_list)):
            for j in range(1,len(name_list[1])): 
                name_list[i][j] = int(name_list[i][j]) 
        return sorted(name_list)

# add the top 10 names for the year to a list       
def find_top_names(lst, year):
    top_names = []
    for row in lst:
        if row[year] <= 5 and row[year] != 0:
            top_names.append(row[0])
    names = ", ".join(top_names)
    return names

#get the year from the user and translate to "decade" column    
def translate_year(year): 
    decade = 0    
    if year == 1900:
        decade = 1
    elif year == 1910:
        decade = 2
    elif year == 1920:
        decade = 3
    elif year == 1930:
        decade = 4
    elif year == 1940:
        decade = 5
    elif year == 1950:
        decade = 6
    elif year == 1960:
        decade = 7
    elif year == 1970:
        decade = 8
    elif year == 1980:
        decade = 9
    elif year == 1990:
        decade = 10
    elif year == 2000:
        decade = 11
    
    if decade != 0:
        print(f'Top five boy\'s and top five girl\'s names for the decade {year}:')
    return decade

# extra credit (searching for a name and returning the rank for each year) 
def get_name_from_user(lst):
    decade_lst = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]
    name_entered = input("Enter a specific name to view the decade stats: ").upper()
    
    name_data = []
    for row in lst:
        row[0] = row[0].upper()
        if row[0] == name_entered:
            name_data.append(row[1:])
    check_if_valid = any(name_entered in sublist for sublist in lst)
    if check_if_valid == False:
        print('You have entered an invalid name.')
        return
        
    print(f'Statistics on {name_entered}:')
    for d, nd in zip(decade_lst, name_data[0]):
        print(f'{d}: {nd}')
    
main()          

# def search_for_top_5_names(d):
#     for i in range(len(d):
#         for k in d:
#             if d[i][1] == 1:
#                 print(k)


#splitting all strings into lists
#entries = []
    # with open('test_names.txt', 'r') as f:
    #     for line in f:
    #         line = line.split()
    #         entries += line
    # print(entries)  
    #return entries

#turns file into dictionary
# def get_file_data_in_dict_form():
#     name_dict = {}
#     with open("test_names.txt", "r") as f:
#         for line in f.readlines():
#             k, *v = line.strip().split(" ")
#             name_dict[k] = v
#         print(name_dict)
#     #need to change values list to int for the for loop to work!!      
#     top_names = []
#     for i in range(1,6):
#         top_names.append([key for key, val in name_dict.items() if i == val[0]])
        
#     return top_names

# print(get_file_data_in_dict_form())