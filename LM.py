import pandas as pd
from collections import OrderedDict
from IPython.display import display
from IPython.display import Image

# print(df_a)
#print(type(raw_data), type(df_a))
# arr= min(raw_data['A'])
# raw_data['A']= arr


def leastMisery(raw_data):

    for key, value in raw_data.items():
        minimo= int(min(value))
        raw_data[key]=minimo
    return raw_data






#
# listOrdered= OrderedDict(sorted(raw_data.items(), reverse=True,key=lambda t: t[1]))
#
# #print(listOrdered)
# lista=[]
# for key,value in listOrdered.items():
#     lista.append(key)
#
# print(lista)