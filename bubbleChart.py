import matplotlib.pyplot as plt
import csv
#import requests
import random
import pandas as pd

data = pd.read_csv('covid_states.csv')
state = data['state']
total_tests = data['totalTestResults']
deaths = data['death']
pos_cases = data['positive']

x_pos = data['positive']
y_death = data['death']
#z_state = data['state']
for x,y in zip(x_pos,y_death):
    for i in range(len(data))
    label = "{}".format(y)
    # this method is called for each point
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') #

plt.scatter(pos_cases, deaths, c=total_tests, alpha=0.75)
cbar = plt.colorbar()
cbar.set_label('Total Number of Tests')

fig = pyplot.figure() 
fig.set_figheight(6) 
fig.set_figwidth(12)

plt.xlabel('Positive Cases')
plt.ylabel('Deaths')
plt.title('Positive Cases vs Deaths vs Total Tests')
plt.yticks([0, 5000, 10000, 20000, 30000])
plt.xticks([0, 200000, 400000, 600000])

plt.tight_layout()
plt.show()




# with open('education.txt') as file:
#     data = file.read()
#     nums = [int(s) for s in data.split() if s.isdigit()]
#     print(nums)
    # for line in data:
    #     parts = data.splitlines()
    # print(parts)
    # dollars = int(parts[1][0])
    # math = int(parts[3][0])
    # science = int(parts[5][0]) 
    # print(science)
    


    # dollars = int(split_data[1][0])
    # math = int(split_data[1][1])
    # science = int(split_data[1][2])
    # print(science)
    #file.close()

# def main():
#     state = ['ca', 'ne', 'ny', 'tx', 'fl', 'ia', 'co', 'ct', 'nj', 'pa']
#     #url = 'https://covidtracking.com/api/v1/states/current.json'

#     for i in range(len(state)):
#         #states = state[i]
#         params = {'state': state[i]}
#         response = requests.get('https://covidtracking.com/api/v1/states/current.json', params=params)
#         usable_response = json.loads(response.text)
    
#     return usable_response

# print(main())

#bubble labels
#x,y = ['math'], ['science']
# for i, text in enumerate('France'):
#     plt.annotate(text, (x[i], y[i]))
#     print(i, text, x[i], y[i], split_data['dollars'][i], split_data['Bubble Color'][i])

# fig = plt.figure()
# fig.set_figheight(8)
# fig.set_figwidth(13)

# with open('education.txt') as file:
#     data = file.read()
#     nums = [int(s) for s in data.split() if s.isdigit()]
#     print(nums)
    # for line in data:
    #     parts = data.splitlines()
    # print(parts)
    # dollars = int(parts[1][0])
    # math = int(parts[3][0])
    # science = int(parts[5][0]) 
    # print(science)
    


    # dollars = int(split_data[1][0])
    # math = int(split_data[1][1])
    # science = int(split_data[1][2])
    # print(science)
    #file.close()

# def main():
#     state = ['ca', 'ne', 'ny', 'tx', 'fl', 'ia', 'co', 'ct', 'nj', 'pa']
#     #url = 'https://covidtracking.com/api/v1/states/current.json'

#     for i in range(len(state)):
#         #states = state[i]
#         params = {'state': state[i]}
#         response = requests.get('https://covidtracking.com/api/v1/states/current.json', params=params)
#         usable_response = json.loads(response.text)
    
#     return usable_response

# print(main())


# x = [520, 527, 504, 548]
# y = [527, 534, 526, 563]
# sizes = [576, 574, 468, 565]
#colors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

