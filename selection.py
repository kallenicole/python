def main():
    lst1 = [4, 62, 783, 1274, 99]
    lst2 = [90, 275, 8, 22, 1.1]
    selection_sort(lst1)
    print()
    selection_sort(lst2)

def selection_sort(values):
    #find smallest and move to beginning
    minval = values[0]
    for i in range(len(values)):
        if values[i] < minval:
            minval = values[i]
    for i in values:
        pos = values.index(minval)
        values[0], values[pos] = values[pos], values[0]
    print(f'The first sort: {values}')
    #find the smallest of the next 4 values and put in 2nd position
    minval2 = values[1]
    for i in range(1, len(values)):
        if values[i] < minval2:
            minval2 = values[i]
    for i in values:
        pos2 = values.index(minval2)
        values[1], values[pos2] = values[pos2], values[1]
    print(f'The second sort: {values}')
    #find the smallest of the last 3 values and put in 3rd position
    minval3 = values[2]
    for i in range(2, len(values)):
        if values[i] < minval3:
            minval3 = values[i]
    for i in values:
        pos3 = values.index(minval3)
        values[2], values[pos3] = values[pos3], values[2]
    print(f'The third sort: {values}')
    
    #find the smallest of the last 2 items and switch if needed
    for i in values:
        if values[3] > values[4]:
            values[3], values[4] = values[4], values[3]
       
    print(f'The fourth and final sort: {values}') 
       

main()


