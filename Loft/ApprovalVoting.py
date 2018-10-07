import pandas as pd
from collections import OrderedDict
from IPython.display import display
from IPython.display import Image

raw_data = {
        'A': [1,0,1],
        'B': [0,1,0],
        'C': [0,1,0],
        'D': [1,1,1],
        'E': [1,1,1],
        'F': [1,1,1],
        'G': [1,1,0],
        'H': [1,1,1],
        'I': [1,0,1],
        'J': [1,1,1],

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