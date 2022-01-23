""" Write a Python program that prompts the user for an integer and then prints
out all the prime numbers up to that integer. For example, if the user enters 20,
the program should print
2
3
5
7
11
13
17
19
 Recall that an integer is prime if it is not divisible by any integer except for 1
and itself. """

def prime():
    chosen_num = int(input("Enter a number: "))
    for chosen_num in range (2, chosen_num):
        prime = True
        for i in range (2, chosen_num):
            if chosen_num % i == 0:
                prime = False
        if prime:
             print(chosen_num)

prime()



""" def prime_num():
    chosen_num = int(input("Enter a number: "))
    for chosen_num in range(2, chosen_num):
        for i in range(2, chosen_num):
            if not chosen_num % i:
                break
        else:
            print (chosen_num)

prime_num() """