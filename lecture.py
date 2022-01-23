# def max_of_three(a, b, c):
#     max = a
#     if b > a:
#         max = b
#     if c > max:
#         max = c
#     return max

# max = max_of_three(3,12,135)
# print(f"The largest is {max}")
# def testing():
#     is_sunny = True
#     has_deck = True
#     is_new = True
#     has_swimming_pool = True
#     is_noisy = False
#     miles_to_harvard = 0
#     rent = 200
#     if (all(is_sunny, has_deck, is_new, has_swimming_pool) and (is_noisy == False) and (miles_to_harvard < 1) and (rent <= 500)):
#         print("I’ll take it!")
#     else:
#         print("No thanks!")
    
# testing()



# def school():
    
#     word = input("What's the word? ")
#     for c in word:
#         print (c, end="_")
#     print()

# school()

# import random

# def die_roll():
#     die1 = random.randint(1,6)
#     die2 = random.randint(1,6)
#     counter = 1
#     while die1 != die2:
#         print(f'{die1}  {die2}')
#         die1 = random.randint(1,6)
#         die2 = random.randint(1,6)
#         counter += 1
#     print(f'They are the same! {die1} {die2} and it took {counter} rolls!')

# die_roll()

# def mystery(x, y):
#     s = '0'
#     while (x > 0 and 2*y >= x):
#         print(s + ' ', end=' ')
#         y = y - x
#         x -= 1
#         s = s + str(2 * x)
#     print(s) 

# mystery(10,31)



# def main():
#     # PROBLEM: Create a method that returns
#     # a new list which is the reverse of the
#     # original
#     original =  [ 9, 1, 7, 3 ]
#     changed = reverse(original)
#     # should be reversed
#     print(changed)

# def reverse(data):
#     for i in range

# main()

# PROBLEM:  What values are stored in the list a after the loop has run?

# def main():
#     a = [ 1, 7, 5, 6, 4, 14, 11 ]
#     for i in range(len(a) - 1):
#         if (a[i] > a[i + 1]):
#             a[i + 1] = a[i + 1] * 2
#     print(a)
    
# main()

#1. Write a function that prints out 5 random numbers between 1 and 5 inclusive
#2. Write a function that creates and returns a list of 5 random numbers

# Now, change 2 such that it returns a list of 5 unique numbers between 1 and 5 
# inclusive (so a permutation of the numbers 1 through 10)  

# import random

# def new_list():
#     random_list = []
#     random_list.append(random.randint(1,3))
#     while len(random_list) < 5:
#         k = random.randint(1,100)
#         #if the random number has already appeared
#         if k not in random_list:
#             random_list.append(k)  
#     return random_list

# print(new_list())




# PROBLEM: Write a linear search method
# that scans through a list and returns
# where the given value can be found
# or -1 if not found

# def main():
#     a =  [ 1, 3, 4, 9, 11, 99, -1, 0 ]
#     print(a)
#     print(search(a, 9))   # should print 3
#     print(search(a, 12))  # should print -1

# def search(a, value):
#     return a.index(value)

# main()



#Write a function that takes a list and a number N, 
#and returns True if any two numbers in the list sum to N.

#What is the runtime of this solution?

#1b. Consider the following problem:  Write a function that takes a list and a number N, 
#and returns True if two adjacent numbers in the list sum to N.What is the runtime of this solution?

# import time

# def main():
#     start_time = time.time()
#     is_sum(([1, 2, 3, 4, 5, 6, 7], 0))
#     print(time.time() - start_time)

# def is_sum(lst, N):
#     for i in range(len(lst)-1):
#         for j in range(i+1, len(lst)):
#             if lst[i] + lst[j] == N:
#                 print(time.time() - start_time)
#                 return True
#     return False    
    
# main()

# import time

# def main():
#     start_time = time.time()
#     print(is_sum([1, 2, 3, 4, 5, 6, 7], 5))
#     print(time.time() - start_time)

# def is_sum(lst, N):
#     for i in range(len(lst)-1):
#         #for j in range(len(lst)-1):
#         if lst[i] + lst[i+1] == N:
#             return True
#     return False    
    
# main()

# def main():
#     pay_rates = [
#          [10.50, 12.00, 14.50, 16.75, 18.00],
#          [20.50, 22.25, 24.00, 26.25, 28.00],
#          [34.00, 36.50, 38.00, 40.35, 43.00],
#          [50.00, 60.00, 70.00, 80.00, 99.99],
#     ]

#     # PROBLEM: Give everyone a $10.00 per hour raise!
#     ???

# main()

# Basically what he’s doing here is taking command line arguments as file names, the first file name AFTER “copy_file.py” 
# (where the code he wants to run is) being the file he wants to copy, and the second file name being the file he wants to copy 
# TO. So sys.argv[1], or the second command line argument after the word “python”, is “poem.txt”, and sys.argv[2], 
# or the third command line argument after the word “python”, is “poem2.txt”Because sys.argv creates  
# a list of all the command line arguments, which in this case would be [“copy_file.py”, “poem.txt”, “poem2.txt”]
# Then he opens file 1, reads it into a variable called contents, closes the file, then opens file 2, writes the 
# contents into file 2, then closes it, effectively copying it over.

#foobar = [1,2,3,4]

#
#for i in range(len(foobar)):


# def square(x, n):
#     if n == 0:
#         return 1
#     elif n > 0:
#         return x * square(x, n-1)
#     else:
#         return 1 / x - square(x, -n)
        
# print(square(2, 3))       

# def mystery(n):
#     if n <= 0:
#         return 0
#     return mystery(n // 2) + 1 

# print(mystery(30))

# def print_triangle (side_length):
#     if side_length < 1 :
#         return
#     print_triangle (side_length-1)
#     print ( "[]"* side_length)

# print_triangle(4)

# def sum_digits(n):
#     s = 0
#     while n:
#         s += n % 10
#         n //= 10
#     return s

# print(sum_digits(1611))



# 1. Recursive sum of list. Write a function to recursively sum a given list.
# a) What is the base case(s)?
# b) What is the recursive case(s)?
# # c) Write the function!
# def sum_of_lst(lst):
#     if len(lst) < 1:
#         return 0
#     else:
#         print(lst)
#         return sum_of_lst(lst[1:]) + lst[0]
        

# print(sum_of_lst([1, 2, 3, 4]))

# 2. Recursive factorial. Write a function that takes a non negative integer and returns its factorial recursively
# a) What is the base case(s)?
# b) What is the recursive case(s)?
# c) Write function!
# def rec_fact(n):
#     if n == 0:
#         return 1
#     else:
#         return rec_fact(n-1) * n

# print(rec_fact(4))


# def power(x, n):
#     if n < 0:
#         return 1.0 / power(x, -n)
#     elif n == 0:
#         return 1
#     elif n % 2 == 0:
#         return x * power(x, n // 2)
#     else:
#         return x * power(x, n - 1)
# print(power(2,3))


# def __add__(self, addition):
#     top = self.getNumerator() + addition.getNumerator()
#     bottom = self.getDenominator()
#     return Rational(top,bottom)

# def foo (x, y, z):
#     print (y, "and", z, "like", x)

# def main():
#     whom = "she"
#     who = "he"
#     it = "her"
#     foo ("it", who, it)
#     foo (it, who, "it")
#     foo (who, it, whom)

# main()

#no idea why this returns none
# def main(): 
#     a = [3, 0, 1, 4, 7]
#     mystery(a)

# def mystery(lis):
#     for i in range(2, len(lis)):
#         lis[i] = lis[i] + lis[i - 1] + lis[i - 2] 
#     return lis

# print(main())


values = [[18, 14, 29], [12, 7], [2, 22, 5]]

def cap(data, big):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] > big:
                data[i][j] = big
    return data

print(cap(values, 2))