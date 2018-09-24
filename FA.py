import pandas as pd
import numpy as np
from collections import OrderedDict

from IPython.display import display
from IPython.display import Image
import itertools, copy


def extractValue(i,df_a, usersNumber):
        # Extracting the i row and calculating the maximum
        rowDf = df_a.loc[i, :]
        maximum = max(rowDf)

        # Finding the letters of max values from an extracted row
        indexMax = rowDf[rowDf == maximum]
        s = list(pd.Series.keys(indexMax))

        # List of Sums that correspond to the higher values into the selected row
        listSums = list()
        for i in range(0, len(s)):
                listSums.append(df_a[s[i]][usersNumber])

        d = dict((key, value) for (key, value) in zip(s, listSums))
        # I've found the column of the maximum element of sums
        maximumColumnLet = max(d, key=d.get)
        # print(maximumColumnLet, d[maximumColumnLet])


        df_b = df_a.drop(columns=maximumColumnLet, axis=1)
        #print(df_b)
        return df_b, maximumColumnLet

        # Creation of empty dict and list

def FairenessAverage(ratingsArraylist, list_POI, list_Names):
    class Engine(object):

        def __init__(self, num):
            self.index = 0

        def valueReturn(self, lista):
            letter = lista[self.index]
            self.index = self.index + 1
            return letter

    final_list = list()


    ratingsArrayPOI = np.array(ratingsArraylist)

    obj = []
    for i in range(len(list_Names)):
        obj.append(Engine(i))

    for i in range(0, len(list_Names)):
        unsorted_df = pd.DataFrame(ratingsArrayPOI, columns=list_POI)
        # print(unsorted_df)

        row = unsorted_df.sort_values(by=i, ascending=False, axis=1)

        # print(row)

        df_a = pd.DataFrame(ratingsArrayPOI, columns=list_POI)
        somma = df_a.sum()
        df_a.loc['Total'] = df_a.sum()

        row = row.append(somma, ignore_index=True)

        # print('\n\n')
        final_list1 = list()
        flattened_list = list()

        for n in range(10, -1, -1):
            vari = row.loc[i, :].where(row.loc[i, :] == n)
            bi = vari.notnull()
            columns = bi.index[bi[0:] == True].tolist()
            if columns != []:
                df1 = pd.DataFrame(row, columns=columns)
                print(df1)
                df1 = df1.sort_values(by=3, ascending=False, axis=1)
                #df1 = df1.sort_values(by=df1.shape[0]-1, ascending=False, axis=1)
                # print(df1)
                columns = df1.columns.tolist()

                final_list1.append(columns)
                final_list2 = list(itertools.chain.from_iterable(final_list1))

            # print(columns)
        final_list.append(final_list2)
    # print(final_list)

    ultimate = list()
    repetition = 2

    while len(ultimate) != len(list_POI):
        for i in range(0, len(list_Names)):
            lista = final_list[i]
            letter = obj[i].valueReturn(lista)
            if (letter not in ultimate):
                ultimate.append(letter)

            if (i == 2):
                for k in range(0, repetition - 1):
                    letter = obj[i].valueReturn(lista)
                    if (letter not in ultimate):
                        ultimate.append(letter)

                for j in range(len(list_Names) - 2, -1, -1):
                    lista = final_list[j]
                    letter = obj[j].valueReturn(lista)
                    if (letter not in ultimate):
                        ultimate.append(letter)
                if (j == 0):
                    for k in range(0, repetition - 2):
                        letter = obj[j].valueReturn(lista)
                        if (letter not in ultimate):
                            ultimate.append(letter)

    print(ultimate)

    return ultimate


    #
    # final_list = list()
    # # Obtaining Users Number and POIs number
    # usersNumber = len(list_Names)
    # poiNumber = len(list_POI)
    #
    #
    # # Building a dataframe from the complete table
    # df_a = pd.DataFrame(ratingsArrayPOI, columns=list_POI)
    # df_a.loc['Total'] = df_a.sum()
    # print(df_a, '\n')
    #
    #
    #
    # while len(df_a.columns)!=0:
    #     for i in range(0,usersNumber):
    #             if(len(df_a.columns)==0):
    #                     break
    #             df_a,maximumColumnLet = extractValue(i,df_a,usersNumber)
    #             final_list.append(maximumColumnLet)
    #             if(i==usersNumber-1):
    #                     for j in range(usersNumber-1,-1,-1):
    #                             if (len(df_a.columns)==0):
    #                                     break
    #                             df_a,maximumColumnLet= extractValue(j,df_a,usersNumber)
    #                             final_list.append(maximumColumnLet)
    #             if (len(df_a.columns)==0):
    #                     break
    # return final_list
    #
