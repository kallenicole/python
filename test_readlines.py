import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def main():
    return makebubbles()

def makebubbles():
    with open('education.txt') as file:
        data = file.readlines()

        #strip carriage returns
        new_list = []
        for i in data:
            new_list.append(i.rstrip('\n'))
        
        #make list of countries
        countries = []
        countries.append(new_list[::2])
        countries = countries[0]

        #extract numbers
        nums = []
        for i in range(1,len(new_list), 2):
            nums.append(new_list[i].split())
        
        #get dollars, math, and science data into lists
        dollars = []
        math = []
        science = []
        for i in range(0, len(nums)):
            dollars.append((int(nums[i][0]))/10)
            math.append(int(nums[i][1]))
            science.append(int(nums[i][2]))
        file.close()

    #make me a scatter plot with a color bar
    figure(figsize=(8, 10), dpi=80, facecolor='w', edgecolor='k')
    plt.scatter(math, science, s=dollars, c=dollars, alpha=0.50)
    cbar = plt.colorbar()
    cbar.set_label('Education Spending Amount (/ 10) per capita ($)')

    #labeling each country
    x_pos = math
    y_pos = science
    z_label = countries
    for x, y, z in zip(x_pos, y_pos, z_label):
        plt.annotate(z, # this is the text
            (x, y), # this is the point to label
            textcoords="offset points", # how to position the text
            xytext=(0,10), # distance from text to points (x,y)
            ha='center') 

    #labeling axes and ticks
    plt.xlabel('Math Scores')
    plt.ylabel('Science Scores')
    plt.title('Math Scores vs Science Scores vs Education Spending')
    plt.yticks([475, 500, 525, 550, 575])
    plt.xticks([475, 500, 525, 550, 575])

    plt.tight_layout()
    plt.show()

main()