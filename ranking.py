from json.decoder import NaN
from saveData import prepareTableCSV
from saveData import saveUserRankings
import numpy as np

def first_rank(listName, listPOI, listCat):
    len_Names= len(listName)
    len_POI = len(listPOI)
    rankingsArrayPOI= np.zeros((len_Names,len_POI))
    #prepareTableCSV(listName)

    for i in range(0,len_Names):
        print('\n\n\n\nHey ', listName[i],', rank these POIs! :)\n\n' )
        for j in range(0, len_POI):
            print(listPOI[j], ' (category: ', listCat[j],')', '\n')
            rankingsArrayPOI[i][j]= int(input('Give your rank (1-10): ---->'))
            print('\n')
        #saveUserRankings(rankingsArrayPOI, listPOI)

    print("Name")
    for i in range(0, len_POI):
        print(listPOI[i])

    print('\n\n')
    for i in range(0,len_Names):
            print(listName[i])
            for j in range(0, len_POI):
                print(int(rankingsArrayPOI[i][j]))
            print('\n\n')
