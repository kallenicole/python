courses = { "CSCI-S7" :
 { "full_name" : "Intro to CS with Python",
 "instructors" : [ "Henry", "Dimitri" ],
 "tas" : ["Amia", "Ben",..., "Zuzanna"],
 "num_homeworks" : 6,
 "num_exams" : 2 },
 
 "FREN-SAA" :
 { "name" : "Beginning French I",
 "num_homeworks" : 5,
 "num_exams" : 2 },
 }
print({ok: {ik: sum(ik.values()) for ik, iv in ov.items()} for ok, ov in courses.items()})

# {key: {key: sum(iv) for key, num_h in ov.items()} for ok, ov in od.items()}
# where
# ok-outer key
# ik-inner key
# ov-outer value
# iv-inner value od-outer dictionary
# sum = 0
# for x, y in courses.items():
#     sum += y['num_homeworks']
# print(sum)
#dict_comp = {(k, v): k+v for k in range(2) for v in range(2)}
#[key for key, val in name_dict.items() if i == val[0]]
#dict_comp = {num_homeworks for num_homeworks in courses.}
#print({: {key: sum(iv) for key, num_h in ov.items()} for ok, ov in od.items()})
#dict_comp = sum(item ["num_homeworks"] for item in courses)
#print(dict_comp)
# {key: {key: sum(iv) for key, num_h in ov.items()} for ok, ov in od.items()}
# where
# ok-outer key
# ik-inner key
# ov-outer value
# iv-inner value od-outer dictionary
# data = {
#     key: {sum(['num_homeworks'].values())} 
#     for key, value in courses.items()
#     for ['num_homeworks'], value2 in courses.items()
# }
# print(data)
# data = {
#     outer_k: {inner_k: myfunc(inner_v)} 
#     for outer_k, outer_v in outer_dict.items()
#     for inner_k, inner_v in outer_v.items()
# }
# dct_sum = {k: sum(['num_homeworks'].values()) for k,  in courses.items()}
# print(dct_sum)
#([sum(courses['num_homeworks'].values()) for ['num_homeworks'] in courses])
#my_dict = (dict((sum(courses.values())) for [key]['num_homeworks'] in courses))