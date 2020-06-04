thisdict = { "P1": ["B", "F", "E"],
             "P2": ["A", "B", "F", "G", "H", "I"],
             "P3": ["C", "B", "E", "F"],
             "P4": ["A", "G"],
             "P5": ["C", "F", "G", "M", "N"]}


def intersection(lst1, lst2):
    return len(list(set(lst1) & set(lst2)))

# for k,v in thisdict.items():
#     print(k,len(v))
#

conteggi= [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# print(intersection(thisdict["P1"], thisdict["P2"]))

def extraction(num):
    conteggi[num]= conteggi[num]+1


v = list(thisdict.values())

for i in range(0,len(thisdict)):
        k=i+1
        if(k <= len(thisdict) ):
            for j in range (k, len(thisdict)):
                print(str(v[i]) + " AND " + str(v[j]))
                print(intersection(v[i], v[j]))
                z= intersection(v[i], v[j])
                extraction(z)
                print("\n")

# for k,v in thisdict.items():
#     print(thisdict.values()[0].keys()[0])

print(conteggi)
