countries = [ "Canada", "Italy",
    "Germany", "Japan",
    "Kazakhstan", "Russia",
    "South Korea", "United States" ]

counts = [
[ 0, 3, 'US' ],
[ 0, 0, 5 ],
[ 0, 0, 1 ],
[ 1, 0, 0 ],
[ 0, 0, 1 ],
[ 3, 1, 1 ],
[ 0, 1, 0 ],
[ 1, 0, 1 ]
]

def medals():
    
    print(("{:13s}{:>10s}{:>10s}{:>10s}{:>10s}").format('', "Gold", "Silver", "Bronze", "Total"))
    for i in range(len(counts)):
        #print(("{:>13s}{:>10d}{:>10d}{:>10d}{:>10d}").format(countries[i], counts[i][0], counts[i][1], counts[i][2], sum(counts[i])))
        print(counts[i][0].index('US'))
medals()