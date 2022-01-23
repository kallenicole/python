def main():
 lst1 = [18, 7, 4, 14, 11]
 lst2 = stretch(lst1)
 print(lst1)
 # the above should print [18, 7, 4, 14, 11]
 print(lst2)
 # the above should print [9, 9, 4, 3, 2, 2, 7, 7, 6, 5]
    
def stretch(lst1):
    new_list = []
    for i in range(len(lst1)):
        if lst1[i] % 2 == 0:
            new_list.append((lst1[i]//2)) 
            new_list.append((lst1[i]//2))
        else:
            new_list.append(lst1[i]-lst1[i]//2)
            new_list.append(lst1[i]//2)     
    return new_list

main()

    