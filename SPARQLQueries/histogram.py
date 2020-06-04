from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import json


file= open("CATtrovati_duplicati.txt", "r", encoding="utf-32")


pois = file.read().splitlines()


file.close()




labels, values = zip(*Counter(pois).items())

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()