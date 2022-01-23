def main():
    return print_triangle(5)

def print_triangle(side_length):
    if side_length:
        print("[]" * side_length)
        print_triangle(side_length - 1)
        return

main()