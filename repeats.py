def print4x():
    print("Controlling complexity is the essence of programming!")
    print("Controlling complexity is the essence of programming!")
    print("Controlling complexity is the essence of programming!")
    print("Controlling complexity is the essence of programming!")

""" def how_many_repeats():
    x = 1
    for i in range(x):
        x = x ** 3  """

def main(what_repeats, how_many_times):
    how_many_times = 1
    for i in range (how_many_times):
        how_many_times = how_many_times ** 3
        print(what_repeats)

main(print4x(), 3)