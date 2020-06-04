import pickle
from collections import Counter

a = open("dict_categories.pickle", "rb")
d = pickle.load(a)

a.close()

# print(Counter(d))
#print(d.get("http://dbpedia.org/resource/Saint_Gregory_the_Illuminator_Church,_Yerevan"))
# print(next(iter(d), 'fail'))
# print(next(iter(d), 'fail'))


# for i in range (52,40,-1):
#     for k,v in d.items():
#         if(len(v)==i):
#             print(i)
#             print(k, v)



# file = open("keys.txt", "w", encoding="utf-8")
# for key, value in d.items():
#
#     file.write(key)
#     file.write('\n')
#
# file.close()