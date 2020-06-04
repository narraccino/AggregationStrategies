import pandas as pd
from collections import OrderedDict
from IPython.display import display
from IPython.display import Image
import itertools, copy

data = {
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
final_Dict = list()
# Obtaining Users Number and POIs number
usersNumber = len(data[list(data.keys())[0]])
poiNumber = len(data.keys())

def prepareTable(data):
        # Creation of empty dict and list
        sum_Dict = dict()

        # Building of the Sum Dictionary
        for key, value in data.items():
                total = sum(value)
                sum_Dict[key] = total

        # Merge of raw_data and Sum Dictionary
        for key, value in data.items():
                data.setdefault(key)
                data[key].append(sum_Dict[key])
        # Building a dataframe from the complete table
        df_a = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])

        return df_a


def extractValue(i):
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
        final_Dict.append(maximumColumnLet)

        df_b = df_a.drop(columns=maximumColumnLet, axis=1)
        #print(df_b)
        return df_b

df_a=prepareTable(data)

print(df_a, '\n')

while len(df_a.columns)!=0:
    for i in range(0,usersNumber):
            if(len(df_a.columns)==0):
                    break
            df_a= extractValue(i)
            if(i==usersNumber-1):
                    for j in range(usersNumber-1,-1,-1):
                            if (len(df_a.columns)==0):
                                    break
                            df_a= extractValue(j)
            if (len(df_a.columns)==0):
                    break


print('The sequence is:\n\n',final_Dict)