import pickle
from tqdm import tqdm

a = open("dict_categories.pickle", "rb")
thisdict = pickle.load(a)
a.close()

# thisdict = { "P1": ["B", "F", "E"],
#              "P2": ["A", "B", "F", "G", "H", "I"],
#              "P3": ["C", "B", "E", "F"],
#              "P4": ["A", "G"],
#              "P5": ["C", "F", "G", "M", "N"]}


letters= { 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7:[], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14:[], 15: [], 16: [], 17: [], 18: [], 19: [], 20: [], 21:[]}



pbar = tqdm(total=len(thisdict))

def intersection(lst1, lst2):
    num = len(list(set(lst1) & set(lst2)))
    return num



def extraction(num, k1, k2):

    if(num>0 and num<20):
        if (k1 not in letters[num]):
            letters[num].append(k1)
        if(k2 not in letters[num]):
            letters[num].append(k2)


v = list(thisdict.values())
chiave= list(thisdict.keys())

for i in range(0,len(thisdict)):
    pbar.update(1)
    k=i+1
    if(k <= len(thisdict) ):
        for j in range (k, len(thisdict)):
            #print(str(v[i]) + " AND " + str(v[j]) + "  " + chiave[i] + " AND " + chiave[j])
            #print(intersection(v[i], v[j]))
            z= intersection(v[i], v[j])
            extraction(z, chiave[i], chiave[j])


pbar.close()
#print(letters)


f= open("conteggi.pickle", "wb")
pickle.dump(letters, f)
f.close()

# a = open("conteggi.pickle", "rb")
# b = pickle.load(a)
# a.close()
#
# print(b)