from json.decoder import NaN
# from saveData import prepareTableCSV
# from saveData import saveUserRankings
from FA import FairenessAverage
import numpy as np

def first_rate(listName, listPOI, listCat):
    len_Names= len(listName)
    len_POI = len(listPOI)
    ratingsArrayPOI= np.zeros((len_Names,len_POI))
    #prepareTableCSV(listName)

    for i in range(0,len_Names):
        print('\n\n\nHey ', listName[i],', rate these POIs : \n\n' )
        for j in range(0, len_POI):
            print(listPOI[j], ' (category: ', listCat[j],')', '\n')
            ratingsArrayPOI[i][j]= int(input('Rate this POI (1-10) or NA: ---->'))
            print('\n')
        #saveUserRankings(rankingsArrayPOI, listPOI)

    # print("Name")
    # for i in range(0, len_POI):
    #     print(listPOI[i])
    #
    # print('\n\n')
    # for i in range(0,len_Names):
    #         print(listName[i])
    #         for j in range(0, len_POI):
    #             print(int(ratingsArrayPOI[i][j]))
    #         print('\n\n')

    final_list=FairenessAverage(ratingsArrayPOI, listPOI, listName)
    print("The ordered list is this:")
    for i in range(0,len_POI):
        print(i+1,'.',final_list[i])