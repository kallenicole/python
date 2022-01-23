N = 5

print("I will average the price of a stock on ", N, "number of days")

my_sum = 0.0
for i in range (N):
    price = float (input ("What is the price on day #", + str(i + 1) + ": "))
    my_sum += price
print ("The average price of the stock =", sum/N)