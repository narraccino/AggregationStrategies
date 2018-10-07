import pandas as pd
from collections import OrderedDict
from IPython.display import display
from IPython.display import Image

raw_data = {
        'A': [10,1,10],
        'B': [4,9,5],
        'C': [3,8,2],
        'D': [6,9,7],
        'E': [10,7,9],
        'F': [9,9,8],
        'G': [6,6,5],
        'H': [8,9,6],
        'I': [10,3,7],
        'J': [8,8,6],

}


for key, value in raw_data.items():
    somma= sum(value)
    raw_data[key]=somma


df_a = pd.DataFrame(raw_data, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], index=[0])
print(df_a)

listOrdered = OrderedDict(sorted(raw_data.items(), reverse=True, key=lambda t: t[1]))

# print(listOrdered)
lista = []
for key, value in listOrdered.items():
    lista.append(key)

print(lista)