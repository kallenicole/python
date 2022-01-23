#i):
def power(x, n):
    if n < 0:
        return 1.0 / power(x, -n)
    elif n == 0:
        return 1
    elif n % 2 == 0:
        return x * power(x, n // 2)
    else:
        return x * power(x, n - 1)

print(power(3,2))


#ii):
#11 calls ...you divide 1024 by 2 eleven times until you get to zero.