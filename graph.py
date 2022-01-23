import matplotlib.pyplot as plt

elements = [500000, 1000000, 2000000, 4000000, 8000000]
growth = [0.0975, 0.1901, 0.3326, 0.7849, 1.4357]

plt.plot(elements, growth)

plt.xlabel('Elements')
plt.ylabel('Runtime in seconds')
plt.title('Runtime Increase Based on Size of Elements - Max_Increase2')
plt.yticks([0, 1, 2, 3])
plt.xticks([5000000, 2000000, 8000000])

plt.show()