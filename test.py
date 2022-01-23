# elements = ['This', 'is', 'a', 'string', 'and']


# for element in elements:
#     print(len(element))

import requests
import string

url = requests.get("http://www.recipepuppy.com/api/?i=soup&p=3")

d={}
total = 0
for i in url.text:
    if i in string.ascii_lowercase:
        if i in d.keys():
            total += 1
            d[i] += 1
        else:
            d[i] = 1
# for key in d:
#     total += d[key]

print(f'We have {d["t"]} ts and we have {d["i"]} is')
print(d)
print(total)