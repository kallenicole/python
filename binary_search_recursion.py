def binary(n, lst):
    if len(lst) == 1:
        return n == lst[0]
    i = len(lst) // 2
    if n < lst[i]:
        return binary(n, lst[:i])
    else:
        return binary(n, lst[i:])

print(binary(5, [1,2,3,4]))