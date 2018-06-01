import pandas as pd
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

def FairenessAverage(ratingsArrayPOI, list_POI, list_Names):
    final_Dict = list()
    # Obtaining Users Number and POIs number
    usersNumber = len(list_Names)
    poiNumber = len(list_POI)


    # Building a dataframe from the complete table
    df_a = pd.DataFrame(ratingsArrayPOI, columns=list_POI)
    df_a.loc['Total'] = df_a.sum()
    print(df_a, '\n')



    while len(df_a.columns)!=0:
        for i in range(0,usersNumber):
                if(len(df_a.columns)==0):
                        break
                df_a,maximumColumnLet = extractValue(i,df_a,usersNumber)
                final_Dict.append(maximumColumnLet)
                if(i==usersNumber-1):
                        for j in range(usersNumber-1,-1,-1):
                                if (len(df_a.columns)==0):
                                        break
                                df_a,maximumColumnLet= extractValue(j,df_a,usersNumber)
                                final_Dict.append(maximumColumnLet)
                if (len(df_a.columns)==0):
                        break
    return final_Dict

