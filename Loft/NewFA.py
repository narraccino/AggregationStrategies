import pandas as pd
import numpy as np
import itertools

class Engine(object):

    def __init__(self,num):
        self.index=0

    def valueReturn(self,lista):
        letter= lista[self.index]
        self.index= self.index+1
        return letter

final_list = list()

ratingsArraylist=list()
ratingsArraylist.append([10,4,3,6,10,9,6,8,10,8])
ratingsArraylist.append([1,9,8,9,7,9,6,9,3,8])
ratingsArraylist.append([10,5,2,7,9,8,5,6,7,6])
ratingsArrayPOI = np.array(ratingsArraylist)
list_POI=list(['A','B','C','D','E','F','G','H','I','J'])
list_Names=list(["Giseppe", "Nava", "Shabnam"])

obj=[]
for i in range(len(list_Names)):
    obj.append(Engine(i))



for i in range(0,len(list_Names)):
    unsorted_df=pd.DataFrame(ratingsArrayPOI,columns=list_POI)
    # print(unsorted_df)

    row= unsorted_df.sort_values(by=i, ascending=False, axis=1)

    df_a=pd.DataFrame(ratingsArrayPOI,columns=list_POI)
    somma= df_a.sum()
    df_a.loc['Total'] = df_a.sum()

    row=row.append(somma, ignore_index=True)


    # print('\n\n')
    final_list1= list()
    flattened_list=list()

    for n in range(10,-1,-1):
        vari= row.loc[i, :].where(row.loc[i, :]==n)
        bi= vari.notnull()
        columns= bi.index[bi[0:]== True].tolist()
        if columns != []:
            df1 = pd.DataFrame(row, columns=columns)
            # print(df1)
            df1= df1.sort_values(by=3, ascending=False, axis=1)
            # print(df1)
            columns= df1.columns.tolist()

            final_list1.append(columns)
            final_list1= list(itertools.chain.from_iterable(final_list1))


        # print(columns)
    final_list.append(final_list1)
print(final_list)



ultimate= list()
repetition=2

while len(ultimate) != len(list_POI):
    for i in range(0, len(list_Names)):
        lista= final_list[i]
        letter= obj[i].valueReturn(lista)
        if(letter not in ultimate):
            ultimate.append(letter)

        if(i==2):
            for k in range(0, repetition-1):
                letter= obj[i].valueReturn(lista)
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
