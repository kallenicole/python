values = [[18, 14, 29], [12, 7], [2, 22, 5]]

def cap(data, big):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] > big:
                data[i][j] = big
    return data

print(cap(values, 2))