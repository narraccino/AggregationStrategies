from itertools import chain
from collections import defaultdict, OrderedDict
import pandas as pd
import numpy as np
import copy

threshold=4



def LeastMostWithout(ratingsArrayPOI, listPOI, listName):

    final_List=list()

    df_a = pd.DataFrame(ratingsArrayPOI,columns = listPOI)
    # print(df_a, '\n')

    df_b= df_a.min()
    df_c = df_a.max()
    df_d = df_b + df_c

    df_a.loc['LM'] = df_b
    df_a.loc['MP'] = df_c
    df_a.loc['Total'] = df_d
    # frames= [df_a, df_b, df_c, df_d]
    # df_d= pd.concat(frames)
    # print(df_a)

    df = copy.deepcopy(df_a)

    for col in df_a.columns:
        truthList = df_a[col] < threshold
        if (True in list(truthList)):
            del df[col]

    # print(df)


    df_final = df.iloc[:, np.argsort(df.loc['Total'])]

    # print(df_final)
    final_List = list(df_final.columns)
    final_List.reverse()
    return final_List, len(final_List)


    # print("The sequence is: ")

    # colonne = list(deflist.keys())
    # # df_a = pd.DataFrame(deflist, columns=colonne, index=[0])
    # # print(df_a)
    #
    # listOrdered = OrderedDict(sorted(deflist.items(), reverse=True, key=lambda t: t[1]))
    #
    # # print(listOrdered)
    # lista = []
    # for key, value in listOrdered.items():
    #     lista.append(key)
    #
    # print('\n\n', lista)


