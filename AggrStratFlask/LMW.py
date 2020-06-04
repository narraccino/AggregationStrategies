# In this code we apply 3 aggregation strategies:
# Least Misery, Most Pleasure, Without Misery.
# In the table of ratings (obtained by users) we added other 3 rows
# the row of Least Misery (on each column we chose the minimum of the column)
# the row of Most Pleasure (on each column we chose the maximum of the column)
# the row of Sum (we have added up LM row and MP row)
# We exclused columns that showed ratings lower of a threshold
# At the end we ordered the list by the SUM row

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


