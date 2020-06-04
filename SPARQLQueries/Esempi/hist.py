from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import pickle

file = open("C:\\Users\\Peppino\\PycharmProjects\\SPARQLQueries\\Esempi\\conteggi.pickle", "rb")
thisdict = pickle.load(file)
file.close()

thisdict = { "P1": ["B", "F", "E"],
             "P2": ["A", "B", "F", "G", "H", "I"],
             "P3": ["C", "B", "E", "F"],
             "P4": ["A", "G"],
             "P5": ["C", "F", "G", "M", "N"]}

v = list(thisdict.values())
chiave= list(thisdict.keys())

pois=list()

for key, value in thisdict.items():
    pois.append(len(value))

print(pois)


# y = [102391, 73753, 39069, 17961, 7245, 3093, 1278, 538, 239, 94, 29, 23, 2, 2, 4, 0, 0, 0, 0, 0, 0]



labels, values = zip(*Counter(pois).items())

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()