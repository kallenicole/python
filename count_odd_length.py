from sys import argv

def count_odd_length():
    input_file = open(argv[1], "r")
    odd = 0
    total = 0
    for line in input_file:
        total += 1
        if len(line) % 2 == 0:
            odd += 1
    print("Total lines =", total)
    print("Lines of odd length =", odd)
    print("% lines of even length =", ((total - odd) / total) * 100)

count_odd_length()