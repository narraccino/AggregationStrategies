from itertools import chain
from collections import defaultdict, OrderedDict
import copy
import pandas as pd

def mergeDictionaries(dict1, dict2):


    dict3 = defaultdict(list)
    for k, v in chain(dict1.items(), dict2.items()):
        dict3[k].append(v)
    return dict3


def match(keys, newlist3):
    lista = copy.deepcopy(newlist3)

    for key, value in newlist3.items():
        if not (key in keys):
            del lista[key]
    return lista

def orderList(deflist):
    colonne = list(deflist.keys())
    # df_a = pd.DataFrame(deflist, columns=colonne, index=[0])
    # print(df_a)

    listOrdered = OrderedDict(sorted(deflist.items(), reverse=True, key=lambda t: t[1]))

    # print(listOrdered)
    lista = []
    for key, value in listOrdered.items():
        lista.append(key)

    print('\n\n', lista)

    return


