def right_triangle():
    num = int(input("Enter a number: "))
    for i in range (num):
        for k in range (i):
            print(' ', end="")
        for j in range (num - i):
            print('#', end="")
        print()

right_triangle()