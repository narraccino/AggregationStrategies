import pandas as pd
from collections import OrderedDict
from IPython.display import display
from IPython.display import Image

raw_data = {
        'A': [8,0,9],
        'B': [1,7.5,1.5],
        'C': [0,4.5,0],
        'D': [2.5,7.5,5.5],
        'E': [8,3,8],
        'F': [6,7.5,7],
        'G': [2.5,2,1.5],
        'H': [4.5,7.5,3.5],
        'I': [8,1,5.5],
        'J': [4.5,4.5,3.5],

}


for key, value in raw_data.items():
    somma= sum(value)
    raw_data[key]=somma


df_a = pd.DataFrame(raw_data, columns=list(raw_data.keys()), index=[0])
print(df_a, '\n\n')


listOrdered = OrderedDict(sorted(raw_data.items(), reverse=True, key=lambda t: t[1]))

# print(listOrdered)
lista = []
for key, value in listOrdered.items():
    lista.append(key)

print(lista)