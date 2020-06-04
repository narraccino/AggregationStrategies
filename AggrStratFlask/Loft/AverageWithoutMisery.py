import pandas as pd
from collections import OrderedDict
from IPython.display import display
from IPython.display import Image
import copy

raw_data = {
    'A': [10, 1, 10],
    'B': [4, 9, 5],
    'C': [3, 8, 2],
    'D': [6, 9, 7],
    'E': [10, 7, 9],
    'F': [9, 9, 8],
    'G': [6, 6, 5],
    'H': [8, 9, 6],
    'I': [10, 3, 7],
    'J': [8, 8, 6],

}

dataset = copy.deepcopy(raw_data)

threshold = int(input('Please insert the threshold value: '))

for key, value in raw_data.items():
    if (min(value) < threshold):
        del dataset[key]

colonne= list(dataset.keys())
#print(colonne)

df_begin = pd.DataFrame(dataset, columns=colonne)
print(df_begin, '\n\n')


for key, value in dataset.items():
    somma= sum(value)
    dataset[key]=somma

colonne= list(dataset.keys())
df_a = pd.DataFrame(dataset, columns=colonne, index=[0])
print(df_a)


listOrdered = OrderedDict(sorted(dataset.items(), reverse=True, key=lambda t: t[1]))

#print(listOrdered)
lista = []
for key, value in listOrdered.items():
    lista.append(key)

print('\n\n',lista)
