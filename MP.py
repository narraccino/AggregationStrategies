import pandas as pd
from collections import OrderedDict
from IPython.display import display
from IPython.display import Image


#print(raw_data)
#print(type(raw_data), type(df_a))
# arr= min(raw_data['A'])
# raw_data['A']= arr

def mostPleasure(raw_data):

    for key, value in raw_data.items():
        maximo= max(value)
        raw_data[key]=maximo

    return raw_data


# df_a = pd.DataFrame(raw_data,columns = ['A', 'B','C','D','E','F','G','H','I','J'],index=[0])
#
# print(df_a)
# listOrdered= OrderedDict(sorted(raw_data.items(), reverse=True,key=lambda t: t[1]))
#
# #print(listOrdered)
#
# lista=[]
# for key,value in listOrdered.items():
#     lista.append(key)
#
# print(lista)
