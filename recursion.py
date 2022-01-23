
#use recursion to return even digits of n ???
# def even_digits(n):
#     if n == 0:
#         return 0
#     else:
#         even_digits(n//10)
#         if n % 2 == 0:
#             return n 
# print(even_digits(2345))


#what does mystery return?
# def mystery(x,y):
#     if y == 1:
#         print(x, end=" ")
#     else:
#         print((x*y), end=" ")
#         mystery(x, y-1)
#         print(", ",(x*y), end="")

# mystery(3,4)

#does the function * by 100, which is zero then add to 50 + 7?
def mystery(x, y):
    if x < 0:
        return -mystery(-x, y)
    elif y < 0:
        return -mystery(x, -y)
    elif x == 0 and y == 0:
        return 0
    else:
        return 100 * mystery(x // 10, y // 10 ) + 10 * (x % 10) + y % 10
print(mystery (5, 7))

# def mystery(n):
#     if n < 1:
#         print(n, end="")
#     else:
#         mystery(n//2)
#         print(", ", n, end="")          #why does it go back down to the else print stmt?
# mystery(14)


#what is this function really doing? adding the digits together.
# def mystery(n):
#     if n < 0:
#         return mystery(-n)
#     elif n < 10:
#         return n
#     else:
#         return n % 10 + mystery(n//10)

# print(mystery(74))


# def mystery(x, y):
#     if x < y:
#         return x
#     else:
#         return mystery(x-y, y)

# print(mystery(20, 13))


# def mystery(n):
#     if n > 100:
#         print(n, end="")
#     else:
#         mystery2(2*n)
#         print(",", n, end="")

# mystery(113)