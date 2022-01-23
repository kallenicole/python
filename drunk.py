import random

def main(N):
    where = ''
    total = 0
    for i in range(N):
        #execute drunk_walk function and assign the second return item to how_many_blocks
        how_many_blocks = drunk_walk()[1]
        #total up the number of blocks walked
        total += how_many_blocks    
        #find out if the first item in list returned is true or false and that will determine home/jail.                    
        if drunk_walk()[0] == True:
            where = 'HOME'
        else:
            where = 'JAIL'
        #print out results of each walk and compute the average at the end of all of the walks
        print('Here we go again...time for a walk!')
        print(f'Walked {how_many_blocks} blocks and landed at {where}!')
        print()
    print(f'Average number of blocks walked is {total / N:.1f}.')


def drunk_walk():
    home = 1            #home is at 1st st
    jail = 11           #jail is at 11th st
    student = 6         #student starts at 6th st
    blocks = 0
    result = []
    while student != home and student != jail:
        #randomly choose a direction to go (negative or positive)
        walk = random.choice([-1,1])
        #walk one block in that direction
        #every time they walk a block, add -1 or 1 to student until student is at 1 or 11
        student += walk
        # +1 to block every time the student walks
        blocks += 1 
        #print(student)
        #print(f'this many blocks have been walked {blocks}')
    #if the student is at 1 they are at home
    #if the student is at 11, they are in jail 
    if student == 1:
        result.append(True)
    else:
        result.append(False)
    #adding the number of blocks walked to the list
    result.append(blocks)
    #return the result of how many blocks the student walked and where they landed (true = home, false = jail)
    return result

main(6)